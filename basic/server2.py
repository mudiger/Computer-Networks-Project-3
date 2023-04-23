import socket
import threading

class Router:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.routing_table = {}
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def send_routing_table(self):
        for neighbor in self.neighbors:
            try:
                message = str(self.routing_table).encode('utf-8')
                socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.connect((neighbor.ip, neighbor.port))
                socket.send(message)
                socket.close()
            except ConnectionRefusedError:
                print(f"Error: {self.name} could not connect to {neighbor.name}")

    def receive_routing_table(self):
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind((self.ip, self.port))
        socket.listen(5)

        while True:
            client_socket, client_address = socket.accept()
            message = client_socket.recv(1024)
            client_socket.close()

            self.routing_table = eval(message.decode('utf-8'))

    def update_routing_table(self):
        for neighbor in self.neighbors:
            new_distance = self.routing_table[neighbor.name] + self.distance_to(neighbor)
            if new_distance < self.routing_table[neighbor.name]:
                self.routing_table[neighbor.name] = new_distance

    def distance_to(self, neighbor):
        if neighbor in self.neighbors:
            return 1
        else:
            return float("inf")

def main():
    router1 = Router("Router1", "192.168.1.1", 5000)
    router2 = Router("Router2", "192.168.1.2", 5001)
    router3 = Router("Router3", "192.168.1.3", 5002)

    router1.add_neighbor(router2)
    router1.add_neighbor(router3)
    router2.add_neighbor(router1)
    router2.add_neighbor(router3)
    router3.add_neighbor(router1)
    router3.add_neighbor(router2)

    threads = []
    for router in [router1, router2, router3]:
        t = threading.Thread(target=router.receive_routing_table)
        t.daemon = True
        t.start()
        threads.append(t)

    while True:
        router1.send_routing_table()
        router2.send_routing_table()
        router3.send_routing_table()

        router1.update_routing_table()
        router2.update_routing_table()
        router3.update_routing_table()

        print(router1.routing_table)
        print(router2.routing_table)
        print(router3.routing_table)

if __name__ == "__main__":
    main()
