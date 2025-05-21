"""7. Write a Program to check if a given graph is a complete graph. Represent the graph
using the Adjacency List representation."""
def is_complete_graph_list(adj_list):
    n = len(adj_list)
    for i in range(n):
        if len(adj_list[i]) != n - 1:
            return False
    return True

# Example
adj_list = [
    [1,2],
    [0,2],
    [0,1]
]
print("Is complete graph:", is_complete_graph_list(adj_list))
