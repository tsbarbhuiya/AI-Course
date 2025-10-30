# 🤖 Algorithm Implementation

This folder contains all AI algorithm implementations covered in our course.  
Each algorithm includes a brief explanation, applications, and its complexity analysis.

---

## 🔹 Uninformed Search Algorithms

1. **Breadth-First Search (BFS)**  
**How it works**: Explores all nodes level by level using a queue (FIFO).  
**Applications**: Shortest path in unweighted graphs, social network analysis.  
**Complexity**:  
- Time: O(b^d)  
- Space: O(b^d)  
*(b = branching factor, d = depth of solution)*

2. **Depth-First Search (DFS)**  
**How it works**: Explores as deep as possible along each branch before backtracking.  
**Applications**: Maze solving, topological sorting, puzzle solving.  
**Complexity**:  
- Time: O(b^d)  
- Space: O(b*d)

3. **Iterative Deepening Search (IDS)**  
**How it works**: Repeatedly applies DFS with increasing depth limits.  
**Applications**: Game tree search where depth is unknown.  
**Complexity**:  
- Time: O(b^d)  
- Space: O(b*d)

4. **Bidirectional Search**  
**How it works**: Runs two simultaneous BFS — one from the start and one from the goal — until they meet.  
**Applications**: Optimal pathfinding in graphs.  
**Complexity**:  
- Time: O(b^(d/2))  
- Space: O(b^(d/2))

5. **Depth-Limited Search (DLS)**  
**How it works**: A variation of DFS with a maximum depth cutoff to prevent infinite recursion.  
**Applications**: Solving problems with known depth limits.  
**Complexity**:  
- Time: O(b^l) *(l = depth limit)*  
- Space: O(b*l)

---

## 🔹 Informed Search Algorithms

1. **Heuristic Search**  
**How it works**: Uses a heuristic function to estimate the cost to reach the goal, improving efficiency.  
**Applications**: Route planning, robotics, AI planning systems.  
**Complexity**: Depends on the heuristic function used.

2. **Best First Search**  
**How it works**: Selects the node with the best heuristic estimate (lowest cost to goal).  
**Applications**: Map routing, network routing.  
**Complexity**:  
- Time: O(b^m)  
- Space: O(b^m) *(m = maximum depth)*

3. **A* Search**  
**How it works**: Combines the cost so far (g) and heuristic estimate (h) to select nodes using `f(n) = g(n) + h(n)`.  
**Applications**: GPS navigation, robot pathfinding, game AI.  
**Complexity**:  
- Time: O(b^d)  
- Space: O(b^d)

4. **AO* Algorithm**  
**How it works**: Works on AND/OR graphs to select the most cost-effective solution path.  
**Applications**: Decision support systems, diagnostic tools.  
**Complexity**: Depends on graph size and structure.

---

## 🔹 Local Search Algorithms

1. **Hill Climbing**  
**How it works**: Starts with a random solution and continuously moves to a better neighboring state.  
**Applications**: Scheduling, layout optimization, pathfinding.  
**Complexity**:  
- Time: O(n)  
- Space: O(1)

2. **Beam Search**  
**How it works**: Explores only the best ‘k’ paths at each level based on heuristic values.  
**Applications**: Speech recognition, machine translation.  
**Complexity**:  
- Time: O(k * b)  
- Space: O(k)

---

## 🔹 Game Algorithms

1. **Minimax Algorithm**  
**How it works**: Explores all possible moves in a game tree, assuming both players play optimally.  
**Applications**: Two-player games like Tic Tac Toe, Chess.  
**Complexity**:  
- Time: O(b^d)  
- Space: O(b*d)

2. **Alpha-Beta Pruning**  
**How it works**: Optimizes Minimax by pruning branches that won’t affect the final decision.  
**Applications**: Games with large search trees like Chess, Checkers.  
**Complexity**:  
- Time: O(b^(d/2)) with good move ordering  
- Space: O(b*d)

---
