import socket
import threading

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 9991

# connect to server
client_socket.connect((host, port))

# function to receive messages from server
def receive_messages():
    while True:
        # receive response from server
        response = client_socket.recv(1024).decode()

        # print response from server
        print(response)

# start a new thread to receive messages from server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# get username from user
username = input('Enter your username: ')

while True:
    # get message from user
    message = input('Enter a message: ')

    # send message to server along with username
    client_socket.send(f'{username}: {message}'.encode())

    # check if user wants to exit
    if message == 'exit':
        break
