import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

clients = []


def send(conn, message):
    name = ""
    for client in clients:
        if client[0] == conn:
            name = client[1]

    message = f"{name} : {message}"

    for client in clients:
        if client[0] != conn:
            client[0].send(message.encode())


def receive(conn, addr):
    while True:
        message = conn.recv(1024).decode()
        if message == "quit":
            break
        send(conn, message)
        name = ""
        for client in clients:
            if client[0] == conn:
                name = client[1]

        print(f"{name} : {message}")
    conn.close()


def main():
    server_socket.listen(5)
    while True:
        conn, addr = server_socket.accept()

        name = conn.recv(1024).decode()
        clients.append([conn, name])

        for client in clients:
            if client[0] != conn:
                client[0].send(f"{name} has joined...".encode())

        print(f"{name} has joined...")

        # started a thread for one client
        threading.Thread(target=receive, args=(conn, addr,)).start()


main()