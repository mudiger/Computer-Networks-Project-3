import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 9991

# connect to server
client_socket.connect((host, port))

while True:
    # get message from user
    message = input('Enter a message: ')

    # send message to server
    client_socket.send(message.encode())

    # check if user wants to exit
    if message == 'exit':
        break

    # receive response from server
    response = client_socket.recv(1024).decode()

    # print response from server
    print(f'Received response from server: {response}')

# close client socket
client_socket.close()
