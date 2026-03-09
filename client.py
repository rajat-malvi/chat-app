import socket
import threading

HOST = '127.0.0.1'
PORT = 5000


def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('utf-8')

        if not message:
            print("\nDisconnected from server")
            break

        print(f"\n{message}")
        print("Message: ", end='', flush=True)


def send_message_to_server(client):
    while 1:
        message = input("Message: ")

        if message.lower() == "/quit":
            client.sendall(message.encode('utf-8'))
            client.close()
            break

        if message.strip() != "":
            client.sendall(message.encode('utf-8'))


def communicate_with_server(client):
    username = input("Enter username: ")

    if not username.strip():
        print("Username cannot be empty")
        return

    client.sendall(username.encode('utf-8'))

    threading.Thread(target=listen_for_messages_from_server, args=(client,), daemon=True).start()

    send_message_to_server(client)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except Exception as e:
        print(f"Error: {e}")
        return

    communicate_with_server(client)


if __name__ == "__main__":
    main()