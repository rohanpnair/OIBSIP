import socket
import threading
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            break
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()
if __name__ == "__main__":
    start_client()