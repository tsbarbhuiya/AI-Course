class State:
    def __init__(self, value):
        self.value = value

    def get_heuristic(self):
      
        return -1 * (self.value - 10) * (self.value - 10) + 100

    def get_neighbors(self):
        return [State(self.value + 1), State(self.value - 1)]

    def __str__(self):
        return f"State{{ value={self.value}, heuristic={self.get_heuristic()} }}"

def hill_climb(initial_state):
    current = initial_state

    while True:
        neighbors = current.get_neighbors()
        next_state = current

        for neighbor in neighbors:
            if neighbor.get_heuristic() > next_state.get_heuristic():
                next_state = neighbor

        if next_state.value == current.value:
            return current  # Local maximum reached

        current = next_state

# Run the hill climbing
initial = State(16)
result = hill_climb(initial)
print("Result:", result)