def minimax(node, is_maximizing, tree):
    
    if isinstance(tree[node], int):
        return tree[node]

    left = tree[node][0]
    right = tree[node][1]
  
    left_best = minimax(left, not is_maximizing, tree)
    right_best = minimax(right, not is_maximizing, tree)

   
    if is_maximizing:
        return max(left_best, right_best)
   
    else:
        return min(left_best, right_best)

# Define the tree
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3,4],
    'E': 5,
    'F': 2,
    'G': 9
}

# Start from root 'A' with maximizing player
best_score = minimax('A', True, game_tree)
print("Best value for the root:", best_score)
