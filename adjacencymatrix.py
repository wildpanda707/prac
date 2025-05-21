"""6. Write a Program to check if a given graph is a complete graph. Represent the graph
using the Adjacency Matrix representation."""
def is_complete_graph_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != 1:
                return False
    return True

# Example
matrix = [
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
print("Is complete graph:", is_complete_graph_matrix(matrix))
