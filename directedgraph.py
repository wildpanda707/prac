"""8. Write a Program to accept a directed graph G and compute the in-degree and outdegree of each vertex"""
def in_out_degrees(graph):
    n = len(graph)
    indegree = [0]*n
    outdegree = [0]*n
    
    for i in range(n):
        outdegree[i] = len(graph[i])
        for j in graph[i]:
            indegree[j] += 1
            
    for i in range(n):
        print(f"Vertex {i}: In-degree = {indegree[i]}, Out-degree = {outdegree[i]}")

# Example
graph = [
    [1, 2],
    [2],
    []
]
in_out_degrees(graph)
