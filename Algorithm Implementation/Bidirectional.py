from collections import deque

# Step 1: Representing the graph
graph = {
    'S': ['1', '2', '3'],
    '1': ['4'],
    '2': ['4', '5'],
    '3': ['5'],
    '4': ['6'],
    '5': ['6'],
    '6': ['7'],
    '7': ['8'],
    '8': ['9', '10'],
    '9': ['11', '12'],
    '10': ['13', '14'],
    '11': ['G'],
    '12': ['G'],
    '13': ['G'],
    '14': ['G'],
    'G': []
}

# Reverse graph for backward search
reverse_graph = {}
for node in graph:
    for neighbor in graph[node]:
        reverse_graph.setdefault(neighbor, []).append(node)

# Step 2: Bidirectional BFS
def bidirectional_bfs(start, goal):
    if start == goal:
        return [start]

    # Initialize queues
    forward_queue = deque([start])
    backward_queue = deque([goal])

    # Visited sets and parent maps
    forward_visited = {start}
    backward_visited = {goal}
    forward_parents = {start: None}
    backward_parents = {goal: None}

    while forward_queue and backward_queue:
        # Expand forward
        if forward_queue:
            current = forward_queue.popleft()
            for neighbor in graph.get(current, []):
                if neighbor not in forward_visited:
                    forward_queue.append(neighbor)
                    forward_visited.add(neighbor)
                    forward_parents[neighbor] = current
                    if neighbor in backward_visited:
                        return build_path(neighbor, forward_parents, backward_parents)

        # Expand backward
        if backward_queue:
            current = backward_queue.popleft()
            for neighbor in reverse_graph.get(current, []):
                if neighbor not in backward_visited:
                    backward_queue.append(neighbor)
                    backward_visited.add(neighbor)
                    backward_parents[neighbor] = current
                    if neighbor in forward_visited:
                        return build_path(neighbor, forward_parents, backward_parents)

    return None

# Step 3: Path Reconstruction
def build_path(meeting_point, forward_parents, backward_parents):
    # Build path from start to meeting point
    path_forward = []
    node = meeting_point
    while node:
        path_forward.append(node)
        node = forward_parents[node]
    path_forward.reverse()

    # Build path from meeting point to goal
    path_backward = []
    node = backward_parents[meeting_point]
    while node:
        path_backward.append(node)
        node = backward_parents[node]

    return path_forward + path_backward

# Run the search
path = bidirectional_bfs('S', 'G')
print("Path from S to G:", path)
