import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 5000
LISTENER_LIMIT = 10
active_clients = []

def listen_for_messages(client, username):
    while 1:
            message = client.recv(2048).decode('utf-8')
                        
            if message.lower() == "/quit":
                remove_client(client, username)
                break
            
            if message != '':
                final_msg = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] [{username}] : {message}'
                send_messages_to_all(final_msg)

def send_message_to_client(client, message):
    client.sendall(message.encode('utf-8'))

def send_messages_to_all(message):
    for user in active_clients: 
        send_message_to_client(user[1], message)

def remove_client(client, username):
    for user in active_clients:
        if user[1] == client:
            active_clients.remove(user)
            break
    
    send_messages_to_all(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [SERVER]:{username} has left")
    client.close()

def client_handler(client):
    try:
        username = client.recv(2048).decode('utf-8')
        if username:
            active_clients.append((username, client))
            send_messages_to_all(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [SERVER]:{username} has joined")
            threading.Thread(target=listen_for_messages, args=(client, username)).start()
    except:
        client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        print(f"Server started on {HOST}:{PORT}")
    except Exception as e:
        return
    
    server.listen(LISTENER_LIMIT)
    
    while 1:
        try:
            client, address = server.accept()
            print(f"Connected: {address[0]}:{address[1]}")
            threading.Thread(target=client_handler, args=(client,)).start()
        except Exception as e:
            break
    
    server.close()

if __name__ == "__main__":
    main()