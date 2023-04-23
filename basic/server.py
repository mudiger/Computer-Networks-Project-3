import socket
import threading

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print(f'Server host: {host}')

# set port number
port = 9991

# bind socket to host and port
server_socket.bind((host, port))

# set the number of client connections that can be queued
server_socket.listen(5)
print('Waiting for a client to connect...')

# list to store all client sockets
client_sockets = []

# function to handle incoming client connections
def handle_client(client_socket, address):
    print(f'Got a connection from {address}')
    client_sockets.append(client_socket)

    while True:
        # receive message from client
        message = client_socket.recv(1024).decode()

        # check if message is empty or client disconnected
        if not message or message == 'exit':
            print(f'{address} disconnected')
            client_sockets.remove(client_socket)
            client_socket.close()
            break

        print(f'Received message from {address}: {message}')

        # send message to all connected clients except the sender
        for socket in client_sockets:
            if socket != client_socket:
                socket.send(f'{address}: {message}'.encode())

# function to listen for incoming client connections
def listen_for_clients():
    while True:
        # accept client connection
        client_socket, address = server_socket.accept()
        # create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# start listening for incoming client connections
client_listener = threading.Thread(target=listen_for_clients)
client_listener.start()
