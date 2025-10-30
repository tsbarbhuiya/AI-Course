import heapq

# Graph: each node maps to a list of tuples (neighbor, cost)
graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('F', 5), ('E', 12)],
    'C': [('D', 7), ('E', 10)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)],
    'G': []
}

# Heuristic values h(n): estimated cost to goal from each node
heuristic = {
    'S': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

def a_star_search(start, goal):
    # Priority queue (min-heap) storing (f(n), g(n), current_node, path)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
   

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            return path, f

        # Explore neighbors
        for neighbor, cost in graph[current]:
            g_new = g + cost                    # g(n) = cost from start to neighbor
            f_new = g_new + heuristic[neighbor] # f(n) = g(n) + h(n)
            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

# Run the algorithm from S to G
path, cost = a_star_search('S', 'G')
print("Path found:", " -> ".join(path))
print("Total cost (f):", cost)
