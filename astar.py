import heapq

goal_state = "GOAL"

# Transition function (state graph)
def transition(state):
    transitions = {
        "A": [("B", 1), ("C", 3)],
        "B": [("D", 2), ("E", 4)],
        "C": [("F", 3), ("G", 5)],
        "D": [("GOAL", 3)],
        "E": [("GOAL", 4)],
        "F": [("GOAL", 3)],
        "G": [("GOAL", 5)]
    }
    return transitions.get(state, [])

# Heuristic function (estimated cost to goal)
def heuristic(state):
    heuristic_values = {
        "A": 6,
        "B": 5,
        "C": 7,
        "D": 3,
        "E": 4,
        "F": 3,
        "G": 5,
        "GOAL": 0
    }
    return heuristic_values.get(state, float('inf'))

# A* Search Algorithm
def astar(start_state):
    frontier = [(heuristic(start_state), 0, start_state)]  # (f_score, cost, state)
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        _, cost, current_state = heapq.heappop(frontier)

        if current_state == goal_state:
            return True  # Goal state found

        if current_state not in explored:
            explored.add(current_state)

            for neighbor, action_cost in transition(current_state):
                heapq.heappush(frontier, (cost + action_cost + heuristic(neighbor), cost + action_cost, neighbor))

    return False  # Goal state not found

# Example usage
start_state = "A"
if astar(start_state):
    print("Goal state found!")
else:
    print("Goal state not reachable.")
