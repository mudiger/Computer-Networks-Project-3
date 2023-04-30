# Saarthak Mudigere Girish (1002119262)
# Chinmay Ramdas Hegde (1002029323)

import json
import socket
import time
import random

# Wait for 2 seconds before sending the message
time.sleep(2)
# Define the neighbor router's IP address and port number
neighbor_ip = "127.0.0.1"
neighbor_port = 5000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the update message repeatedly every 5 seconds
n=0
while n<3:
    source = ["127.0.0.1", "127.0.0.2", "127.0.0.3", "127.0.0.4", "127.0.0.5", "127.0.0.6"]
    random_source = random.choice(source)
    random_cost = random.randint(0, 4)
    if random_source=="127.0.0.1":
        destination = ["127.0.0.2", "127.0.0.5", "127.0.0.6"]
        random_destination = random.choice(destination)
    elif random_source=="127.0.0.2":
        destination = ["127.0.0.1", "127.0.0.4", "127.0.0.6"]
        random_destination = random.choice(destination)
    elif random_source=="127.0.0.3":
        destination = ["127.0.0.4", "127.0.0.6"]
        random_destination = random.choice(destination)
    elif random_source=="127.0.0.4":
        destination = ["127.0.0.2", "127.0.0.3"]
        random_destination = random.choice(destination)
    elif random_source=="127.0.0.5":
        destination = ["127.0.0.1", "127.0.0.6"]
        random_destination = random.choice(destination)
    else:
        destination = ["127.0.0.1", "127.0.0.2", "127.0.0.3", "127.0.0.5"]
        random_destination = random.choice(destination)
    # Define the update message
    update = {
        "source": random_source,
        "destination": random_destination,
        "cost": random_cost
    }
    # Send the update message to the neighbor router
    print("\nSending update message:", update)
    sock.sendto(json.dumps(update).encode(), (neighbor_ip, neighbor_port))
    # Wait for 4 seconds before sending the message again
    n+=1
    time.sleep(4)
