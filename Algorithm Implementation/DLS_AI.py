explored = set()
path = []
found = False

def depth_limited_search(network, current, depth, limit, goal):
    global found  
    if found:
        return
    if current == goal:
        found = True
        path.append(current)
        return
    if depth > limit:
        return
    if current not in explored:
        path.append(current)
        explored.add(current)
        for adjacent in network[current]:
            depth_limited_search(network, adjacent, depth + 1, limit, goal)

network = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}

depth_limited_search(network, 'A', 0, 2, 'F')
print("->".join(path))