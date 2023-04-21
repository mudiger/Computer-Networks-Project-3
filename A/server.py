import argparse
import socket
import display_script

def listening():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Listen on a UDP port')
    parser.add_argument('port', type=int, help='UDP port to listen on')

    # Parse the command line arguments
    args = parser.parse_args()

    HOST = 'localhost'  # server hostname or IP address
    #PORT = 8888  # port to listen on
    '''FILENAME = 'routers.config'  # name of the file to send

    # read the file contents
    with open(FILENAME, 'rb') as f:
        file_data = f.read()

    print(file_data)'''

    # create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind the socket to a specific address and port
        s.bind((HOST, args.port))

        # listen for incoming connections
        s.listen()
        #print(f"Listening on UDP port {args.port}...")
        print(f"\nListening on UDP: {HOST} with port: {args.port}") 

        while True:
            # accept a connection
            conn, addr = s.accept()
            print(f"Connected by {addr}")

            with conn:
                # send the file data to the client
                conn.sendall(display_script)

display_script
listening()

    


