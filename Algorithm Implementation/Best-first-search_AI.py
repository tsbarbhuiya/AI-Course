import heapq
# Graph structure (with edge costs, although not used in greedy best-first)
graph = {
    'A': [('B', 11), ('C', 4), ('D', 7)],
    'B': [('E', 15)],
    'C': [('E', 10), ('F', 12)],
    'D': [('F', 25)],
    'E': [('H', 9)],
    'H': [('G', 10)],
    'F': [('G', 20)],
    'G': [],
}

# Heuristic values (from node A to G)
heuristic = {
    'A': 40,
    'B': 10,
    'C': 35,
    'D': 25,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0,
}

def best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    visited = []
    while open_list:
        _, current = heapq.heappop(open_list)
        visited.append(current)

        if current == goal:
            break

        # Add items to open list
        for item, _ in graph[current]:
            if item not in open_list:
                heapq.heappush(open_list, (heuristic[item], item))  
    return "->".join(visited)

print(best_first_search('A', 'G'))
              