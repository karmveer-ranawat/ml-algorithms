import heapq

def best_first_search(graph, heuristics, start, goal):
    # Priority queue to store (heuristic cost, node, path)
    pq = [(heuristics[start], start, [])]  # (heuristic cost, current node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)  # Expand the least heuristic cost node

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        # Goal check
        if node == goal:
            print(f"Path found: {' -> '.join(path)}")
            return path

        # Explore neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path))

    print("Goal not reachable.")
    return None

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

# Heuristic values (estimated cost to goal 'H')
heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 3,
    'G': 6,
    'H': 0  # Goal node heuristic is always 0
}

start_node = 'A'
goal_node = 'H'

print("Best First Search Result:")
best_first_search(graph, heuristics, start_node, goal_node)
