from collections import deque
def breadth_first_search(network, start):
    visited = set()
    queue = deque([start]) 
    while queue:
        current = queue.popleft()
        if current not in visited:
            print(current)
            visited.add(current)
            for item in network[current]:
                if item not in visited:
                    queue.append(item)

# Graph network (same as your DFS one)
network = {
    'S': ['A', 'B'], 
    'A': ['C','D'],
    'C': ['E', 'F'],
    'E': ['K'],
    'K': [],
    'F': [],
    'D': [],
    'B': ['G', 'H'],
    'G': ['I'],
    'H': [],
    'I': [],
}
breadth_first_search(network, 'S')










