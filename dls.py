#Iterative Depth-Limited Search (DLS)

def depth_limited_search_iterative(graph, start, goal, depth_limit):
    stack = [(start, 0)]  # Stack contains tuples of (node, current_depth)

    while stack:
        node, depth = stack.pop()

        # Print visited node
        print(node, end=" ")

        # Goal check
        if node == goal:
            print("\nGoal found!")
            return True

        # Expand node only if depth limit is not reached
        if depth < depth_limit:
            for neighbor in reversed(graph.get(node, [])):  # Reverse to maintain correct order
                stack.append((neighbor, depth + 1))

    print("\nGoal not found within depth limit.")
    return False

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

depth_limit = 3
goal_node = 'H'

print("Iterative DLS Search:")
depth_limited_search_iterative(graph, 'A', goal_node, depth_limit)
