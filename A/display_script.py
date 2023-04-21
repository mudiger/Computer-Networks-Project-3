'''#import argparse

FILENAME = 'routers.config'  # name of the file to send
#parser = argparse.ArgumentParser(description='Display router configuration')
def display():#parser.add_argument('config_file', type=str, help='Path to configuration file')):
    # Set up the argument parser
    # Parse the command line arguments
    #args = parser.parse_args()

    # Read the configuration file
    #with open(args.config_file) as f:
    #    lines = f.readlines()

    

    # read the file contents
    with open(FILENAME, 'rb') as f:
        lines = f.readlines()

    
    # Extract the neighbor information
    neighbors = []
    for line in lines:
        line = line.strip()
        if line():# and not line.startswith('#'):
            parts = line.split()
            neighbors.append((parts[0], parts[1], int(parts[2])))

    # Print the neighbor information
    #print(f"Directly connected neighbors of Router 1:")
    for neighbor in neighbors:
        print(f"{neighbor[0]} {neighbor[1]} (cost {neighbor[2]})")


def main():
    display()
    


if __name__ == "__main__":
    main()'''

with open('routers.config', 'r') as f:
    for line in f:
        print(line.strip())
