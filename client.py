import socket
import threading

host = "100.64.65.186"
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))


def send():
    while True:
        message = input()
        client_socket.send(message.encode())


def receive():
    print(client_socket.recv(1024).decode())
    while True:
        message = client_socket.recv(1024).decode()
        print(message)


name = input("Enter your name: ")
client_socket.send(name.encode())


t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)

t1.start()
t2.start()
