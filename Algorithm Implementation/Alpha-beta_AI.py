

def alphabeta(current, game_tree, level, alpha, beta, is_maximizing):
    if not game_tree[current]['children']:
        return game_tree[current]['value']

    if is_maximizing:
        max_score = float('-inf')
        for next_node in game_tree[current]['children']:
            score = alphabeta(next_node, game_tree, level + 1, alpha, beta, False)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = float('inf')
        for next_node in game_tree[current]['children']:
            score = alphabeta(next_node, game_tree, level + 1, alpha, beta, True)
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score

def get_optimal_value(source, game_tree):
    optimal_score = alphabeta(source, game_tree, 0, float('-inf'), float('inf'), True)
    return optimal_score


game_tree = {
    'A': {'children': ['B', 'C'], 'value': None},
    'B': {'children': ['D', 'E'], 'value': None},
    'C': {'children': ['F', 'G'], 'value': None},
    'D': {'children': [], 'value': 3},
    'E': {'children': [], 'value': 5},
    'F': {'children': [], 'value': 2},
    'G': {'children': [], 'value': 9},
}


optimal_value = get_optimal_value('A', game_tree)
print(f"The optimal value from node 'A' is: {optimal_value}") 