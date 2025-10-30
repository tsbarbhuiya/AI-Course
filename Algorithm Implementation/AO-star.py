# AO* Graph node representation
graph = {
    'A': [('B', 1), ('C', 1), ('D', 1)],  # OR between B, C, D
    'B': [('E', 1), ('F', 1)],            # AND between E and F
    'C': [('G', 1), ('H', 1), ('I', 1)],  # AND between G, H, I
    'D': [],                              # Terminal node
    'E': [], 'F': [], 'G': [], 'H': [], 'I': []  # Terminal nodes
}

# Heuristic values from the image
heuristics = {
    'A': 7,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 4,
    'G': 2,
    'H': 0,
    'I': 0
}

# Visited states
solution_graph = {}

def get_successors(node):
    return graph.get(node, [])

def minimum_cost_child_node(node):
    # AND case: for B -> E & F, or C -> G, H, I
    children = get_successors(node)
    
    if not children:
        return None, heuristics[node]

    # Handle AND-case if multiple children
    if node in ['B', 'C']:  # From image, B and C are AND-nodes
        cost = sum(c for _, c in children) + sum(heuristics[child] for child, _ in children)
        return [child for child, _ in children], cost
    else:  # OR-node (like from A)
        min_cost = float('inf')
        best_child = None
        for child, cost_to_child in children:
            total_cost = cost_to_child + heuristics[child]
            if total_cost < min_cost:
                min_cost = total_cost
                best_child = child
        return best_child, min_cost

def AOStar(node, backtrack=False):
    print(f"Processing Node: {node}")
    if node not in graph or not graph[node]:
        return

    child_node, cost = minimum_cost_child_node(node)
    heuristics[node] = cost
    solution_graph[node] = child_node

    # If AND-node (child_node is list), do recursive AO* on all children
    if isinstance(child_node, list):
        for child in child_node:
            AOStar(child)
    else:
        AOStar(child_node)

def print_solution(node, indent=""):
    if node not in solution_graph:
        print(indent + node)
        return
    print(indent + str(node))
    child = solution_graph[node]
    if isinstance(child, list):
        for ch in child:
            print_solution(ch, indent + "  ")
    else:
        print_solution(child, indent + "  ")

# Run AO* from start node
AOStar('A')
print("\nOptimal Solution Path:")
print_solution('A')
