def check_edge(adjacency_matrix, node1, node2):
    if adjacency_matrix[node1][node2] == 1:
        return 1
    else:
        return -1

# Приклад використання:
adjacency_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

node1 = 0
node2 = 1

print(check_edge(adjacency_matrix, node1, node2))  # Виведе 1

node1 = 0
node2 = 2

print(check_edge(adjacency_matrix, node1, node2))  # Виведе -1
