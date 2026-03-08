import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message!='':
            username = message.split("#")[0]
            msg = message.split("#")[1]

            print(f"{username}: {msg}")

        else:
            print("Message is empty")

def send_message_to_server(client):
    while 1:

        message = input("Message: ")
        if message!="":
            client.sendall(message.encode('utf-8'))
        else:
            print("Message cannot be empty")

def communicate_with_server(client):
    username = input("Enter username: ")
    if username!="":
        client.sendall(username.encode('utf-8'))
    else:
        print("Username cannot be empty")
        return
    
    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()
    send_message_to_server(client)


def main():
    # creating socket object for client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    try:    
        client.connect((HOST, PORT))
    except Exception as e:
        print(f"Error: {e}")
        return
    
    communicate_with_server(client)


if __name__ == "__main__":
    main()