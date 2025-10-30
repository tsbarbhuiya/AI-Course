explored = set()
def depth_first_search(explored, network, current):
    if current not in explored:
        print(current)
        explored.add(current)
        for adjacent in reversed(network[current]):
            depth_first_search(explored, network, adjacent)
network = {
    'S': ['A', 'H'],
    'A': ['B', 'C'],
    'B': ['D','E'],
    'C': ['G'],
    'D': [],
    'E': [],
    'G': [],
    'H': ['I', 'J'],
    'I': ['K'],
    'J': [],
    'K': [],   
}
depth_first_search(explored, network, 'S') 



