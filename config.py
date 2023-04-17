import pandas as pd

topology_table = {
    'A': [('B', 4), ('E', 2), ('F', 6)],
    'B': [('A', 4), ('D', 3), ('F', 1)],
    'C': [('D', 1), ('F', 1)],
    'D': [('B', 3), ('C', 1)],
    'E': [('A', 2), ('F', 3)],
    'F': [('A', 6), ('B', 1), ('C', 1), ('E', 3)]
}

data = {'Router': [], 'Connected Router': [], 'Weight': []}

for router, connections in topology_table.items():
    for connection, weight in connections:
        data['Router'].append(router)
        data['Connected Router'].append(connection)
        data['Weight'].append(weight)

df = pd.DataFrame(data)
