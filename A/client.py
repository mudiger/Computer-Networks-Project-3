import socket

HOST = 'localhost'  # server hostname or IP address
PORT = 5000  # port to connect to

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((HOST, PORT))

    # send data to the server
    #s.sendall(b'Hello, world!')

    # receive data from the server
    data = s.recv(1024)

print(f"Received {data} from server")
