import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print(host)
print(socket.gethostbyname(host))

# set port number
port = 9991

# bind socket to host and port
server_socket.bind((host, port))

# set the number of client connections that can be queued
server_socket.listen(1)

print('Waiting for a client to connect...')

# accept client connection
client_socket, address = server_socket.accept()

print(f'Got a connection from {address}')

while True:
    # receive message from client
    message = client_socket.recv(1024).decode()

    # check if message is empty or client disconnected
    if not message or message == 'exit':
        print('Client disconnected')
        break

    print(f'Received message from client: {message}')

    # send message to client
    response = input('Enter a response: ')
    client_socket.send(response.encode())

# close client and server sockets
client_socket.close()
server_socket.close()
