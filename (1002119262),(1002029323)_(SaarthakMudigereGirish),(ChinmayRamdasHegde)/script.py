# Saarthak Mudigere Girish (1002119262)
# Chinmay Ramdas Hegde (1002029323)

import argparse
import socket
from collections import defaultdict
import re
from datetime import datetime, timezone
import subprocess



# Set up the argument parser
parser = argparse.ArgumentParser(description='Display router configuration')
parser.add_argument('port', type=str, help='Path to configuration file')
parser.add_argument('config_file', type=str, help='Path to configuration file')

# Parse the command line arguments
args = parser.parse_args()

# Read in the graph data from a file
graph = defaultdict(dict)

# Read the configuration file
with open(args.config_file) as f:
    lines = f.readlines()
    for line in lines:
        node1, node2, weight = line.strip().split()
        graph[node1][node2] = int(weight)
        #graph[node2][node1] = int(weight)
        print(f"{node1} -> {node2} (cost {weight})")


flag=0
def bellman_ford(graph, start):
    global flag
    # Step 1: Initialize distances from the start node to all other nodes to infinity
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    
    # Step 2: Relax edges repeatedly
    for i in range(len(graph)):
        changed = False
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:                 
                    distances[neighbor] = distances[node] + weight
                    changed = True
        if not changed:
            # No distance values were updated in this iteration, so stop
            print("Algorithm stopped after", i+1, "iterations")
            flag+=i+1
            return dict(distances)

    # Step 3: Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError('Graph contains a negative-weight cycle')

    # Step 4: Return the distances
    print(f"Program converged after running for {flag} times")
    return dict(distances)


# Read the configuration file to create a set
with open(args.config_file) as f:
    lines = f.readlines()

# Extract the neighbor information
neighbors = []
for line in lines:
    line = line.strip()
    if line and not line.startswith('#'):
        parts = line.split()
        neighbors.append((parts[0], parts[1],int(parts[2])))



# Creat set per node
lst_rt=set()
for i in neighbors:
    lst_rt.add(i[0])
# Use the Bellman-Ford algorithm to find the shortest paths from node 127.0.0.1
for i in sorted(lst_rt):
    print("\n-----------------", i,"-----------------")
    shortest_paths = bellman_ford(graph, i)
    # Print the shortest paths
    for node, distance in shortest_paths.items():
        print(f'Shortest path from {i} to {node}: {distance}')
    if i == "127.0.0.6":
        print(f"\nTotal number of updates value (n): {flag}")

try:
    # Read the port number
    port = int(args.port)
    ip_address = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip_address, port))
    print(f"Router Listening on port {port}")
    update=0 # Initialize update number
    subprocess.Popen(['python', r'C:\Users\Saarthak Mudigere\Desktop\(1002119262),(1002029323)_(SaarthakMudigereGirish),(ChinmayRamdasHegde)\client.py'])
    payload_size = 0  # Initialize payload size

    while True:
        for i in lst_rt:
                #print(node,'---->node')
                # Listen for updates
            count=0
            flag=0
            while count<1:
                count+=1
                data, addr = sock.recvfrom(1024)
                recv_message = data.decode('utf-8')
                # Get the size of the payload in bytes
                payload_size = len(data)

                # Initialize an empty dictionary
                message = []

                # Parse the lines into key-value pairs  
                value = recv_message.split(',')
                message.append(value)
                    
                pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                pattern2 = r'\d+'
                matches = re.findall(pattern, recv_message)
                matches2 = re.findall(pattern2, recv_message)

                # Find the source, destination, and cost using regex
                source = matches[0]
                destination = matches[1]
                cost = matches2[-1]
                prev_cost = graph[source][destination]
                    
                # Change the link cost
                graph[source][destination] = int(cost)
                graph[destination][source] = int(cost)

                update+=1
                print(f"\nSource: {source}")
                print(f"Current Cost: {graph[source][destination]}")
                print(f"Previous Cost: {prev_cost}")

                name = {"127.0.0.1":"A", "127.0.0.2":"B", "127.0.0.3":"C", "127.0.0.4":"D", "127.0.0.5":"E", "127.0.0.6":"F"}
                print(f"\n---------------AFTER UPDATE {update}---------------")
                # Use the Bellman-Ford algorithm to find the shortest paths
                for i in sorted(lst_rt):
                    print("\n-----------------", i,"-----------------")
                    shortest_paths = bellman_ford(graph, i)
                    # Print the shortest paths
                    for node, distance in shortest_paths.items():
                        print(f'Shortest path from {i} to {node}: {distance}')
                    if i == "127.0.0.6":
                        print(f"\nMessage from Router(Name: {name[source]}, IP address: {source}, Port No.: {port})")
                        print("Your UTA-ID number(s): 1002119262, 1002029323")     
                        # Get the current local time
                        current_time = datetime.now(timezone.utc)
                        print(f"The date and timestamp in UTC: {current_time}")
                        print(f"Total number of updates value (n): {flag}")
                        print(f"Payload size exclusively for this last broadcast: {payload_size}")
                        
            if update==3:                
                exit(0)
except socket.error as e:
    print('Socket error: ' + str(e))

finally:
    # close the socket
    try:
        sock.close()
        print('Socket closed')
    except socket.error as e:
        print('Failed to close socket: ' + str(e))