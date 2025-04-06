import heapq
def uniform_cost_search(graph, start, goal):
# Priority queue to store (cost, node, path)
pq = [(0, start, [])] # (cumulative cost, current node, path)
visited = set()
while pq:
cost, node, path = heapq.heappop(pq) # Get node with the lowest cost
if node in visited:
continue
visited.add(node)
path = path + [node]
# Goal test
if node == goal:
print(f"Optimal Path: {' -> '.join(path)}, Total Cost: {cost}")
return path, cost
# Explore neighbors
for neighbor, edge_cost in graph.get(node, []):
if neighbor not in visited:
heapq.heappush(pq, (cost + edge_cost, neighbor, path))
print("Goal not reachable.")
return None, float('inf')
graph = {
'A': [('B', 1), ('C', 4)],
'B': [('D', 2), ('E', 5)],
'C': [('F', 3)],
'D': [('G', 1)],
'E': [('G', 2)],
'F': [('G', 5)],
'G': []
}
start_node = 'A'
goal_node = 'G'
print("Uniform Cost Search Result:")
uniform_cost_search(graph, start_node, goal_node)
