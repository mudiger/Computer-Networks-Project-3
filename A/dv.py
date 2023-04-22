import socket
import sys
import time

# Get port number from command line arguments
if len(sys.argv) != 2:
    print("Usage: python router.py <port>")
    sys.exit(1)
port = int(sys.argv[1])

# Read configuration from router.config file
with open('router.config', 'r') as f:
    config_lines = f.readlines()

# Create dictionary to store neighbor information
neighbors = {}
for line in config_lines:
    router_ip, neighbor_ip, cost = line.strip().split()
    cost = int(cost)
    if router_ip not in neighbors:
        neighbors[router_ip] = []
    neighbors[router_ip].append((neighbor_ip, cost))

# Initialize distance vector with self as source and infinite cost to other routers
distance_vector = {router_ip: {router_ip: 0} for router_ip in neighbors}
for router_ip, neighbor_list in neighbors.items():
    for neighbor_ip, cost in neighbor_list:
        if neighbor_ip not in distance_vector:
            distance_vector[neighbor_ip] = {router_ip: float('inf')}
            socks[neighbor_ip] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socks[neighbor_ip].bind((router_ip, port))
        distance_vector[router_ip][neighbor_ip] = cost

# Print initial distance vector
print("Initial distance vector:")
for router_ip, vector in distance_vector.items():
    print(f"Router {router_ip} has distance vector {vector}")

# Send initial distance vector to neighbors
for neighbor_ip in neighbors.keys():
    data = f"{router_ip} {distance_vector[router_ip]}"
    socks[neighbor_ip].sendto(data.encode(), (neighbor_ip, port))

# Wait for incoming messages and update distance vector as needed
while True:
    for neighbor_ip, sock in socks.items():
        data, address = sock.recvfrom(1024)
        source_ip, source_vector = data.decode().split()
        source_vector = eval(source_vector)
        updated = False
        for dest_ip, cost in source_vector.items():
            new_cost = cost + distance_vector[router_ip][source_ip]
            if dest_ip not in distance_vector[router_ip] or new_cost < distance_vector[router_ip][dest_ip]:
                old_cost = distance_vector[router_ip].get(dest_ip, float('inf'))
                distance_vector[router_ip][dest_ip] = new_cost
                updated = True
                print(f"Update received from {source_ip}: {dest_ip} cost changed from {old_cost} to {new_cost}")
        if updated:
            # Send updated distance vector to all neighbors
            for neighbor_ip in neighbors.keys():
                data = f"{router_ip} {distance_vector[router_ip]}"
                socks[neighbor_ip].sendto(data.encode(), (neighbor_ip, port))
    time.sleep(1)  # Wait 1 second before checking for updates again
