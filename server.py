import socket
# for handling multiple clients
import threading
HOST = '127.0.0.1'
PORT = 5000
LISTENER_LIMIT = 3
active_clients = []


def listen_for_messages(client, username):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message!='':
            final_msg = username + "# " + message
            send_messages_to_all(final_msg)
            

# function to sent msg a single client
def send_message_to_client(client, message):
    client.sendall(message.encode('utf-8'))

# sent msg to all clients that are currently connected to the server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)



def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username:
            active_clients.append((username, client))
            break
        
            
    threading.Thread(target=listen_for_messages, args=(client, username)).start()


def main():
    # cearing socket class object
    # socket -> module, socket -> class
    # AF_INET -> IPV4 addr, 
    # SOCK_STREAM -> TCP, UDP -> SOCK_DGRAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind server with host and port
    try:
        # bind -> bind the server to the host and port
        server.bind((HOST, PORT))
        print(f"Server started on {HOST}:{PORT}")
    except Exception as e:
        print(f"Error: {e}")
        return

    # set configurations 
    server.listen(LISTENER_LIMIT)

    # this while loop will keep the server running and accepting clients
    while 1:
        client, address = server.accept()
        print(f"Client connected from Host: {address[0]}, Port: {address[1]}")
        
        threading.Thread(target=client_handler, args=(client,)).start()
        
if __name__ == "__main__":
    main()