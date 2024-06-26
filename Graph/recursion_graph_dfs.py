def dfs_with_weights(node, visited, graph):
    if node not in visited:
        print(node)  # Process the current node
        visited.add(node)
        
        # Get the neighbors sorted by the edge weights
        neighbors = sorted(graph[node], key=lambda x: x[1])
        
        for neighbor, weight in neighbors:
            if neighbor not in visited:
                dfs_with_weights(neighbor, visited, graph)

# Example graph
"""
        A
       / \
      2   3
     /     \
    B       C
   / \       \
  1   4       5
 /     \       \
D       E-------F
             1
"""
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 1), ('E', 4), ('A',2)],
    'C': [('F', 5), ('A', 3)],
    'D': [('B', 1)],
    'E': [('F', 1), ('B',4)],
    'F': [('E',1), ('C', 5)]
}

visited = set()
dfs_with_weights('A', visited, graph)

#Aap yeh code mere gihub location se be le sakete hai maine github ka link description me mention kr diya hu.