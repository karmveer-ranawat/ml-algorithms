#Recursive DFS (AI Style Search)

def dfs_recursive(graph, node, goal, visited=None):
    if visited is None:
        visited = set()

    # Mark the node as visited
    visited.add(node)
    print(node, end=" ")

    # Check if the goal is found
    if node == goal:
        print("\nGoal found!")
        return True

    # Explore neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_recursive(graph, neighbor, goal, visited):
                return True  # Goal found, stop further exploration

    return False  # Goal not found in this path

#Example Usage (AI Graph Search Scenario)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

print("Recursive DFS:")
dfs_recursive(graph, 'A', 'H')
