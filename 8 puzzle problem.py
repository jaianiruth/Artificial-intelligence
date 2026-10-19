import heapq

# Goal state for the 8-puzzle
GOAL_STATE = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

class Node:
    def __init__(self, state, parent=None, move="", depth=0, cost=0):
        self.state = state          # Tuple representing the 3x3 board
        self.parent = parent        # Parent node
        self.move = move            # Move taken to reach this state
        self.depth = depth          # g(n): cost from start
        self.cost = cost            # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.cost < other.cost

def get_manhattan_distance(state):
    """Calculates the Manhattan distance heuristic for the state."""
    distance = 0
    for i, value in enumerate(state):
        if value == 0:
            continue
        # Find goal position for this value
        goal_idx = GOAL_STATE.index(value)
        curr_row, curr_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_idx, 3)
        distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

def get_neighbors(node):
    """Generates valid neighboring states by moving the empty tile (0)."""
    neighbors = []
    zero_idx = node.state.index(0)
    row, col = divmod(zero_idx, 3)
    
    # Possible directions: (row_change, col_change, move_name)
    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_idx = new_row * 3 + new_col
            # Swap 0 with the neighbor
            state_list = list(node.state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            
            new_state = tuple(state_list)
            g = node.depth + 1
            h = get_manhattan_distance(new_state)
            neighbors.append(Node(new_state, node, move, g, g + h))

    return neighbors

def solve_8_puzzle(start_state):
    """Solves the 8-puzzle problem using A* search algorithm."""
    start_node = Node(start_state, None, "", 0, get_manhattan_distance(start_state))
    open_set = []
    heapq.heappush(open_set, start_node)
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.state == GOAL_STATE:
            path = []
            while current.parent:
                path.append((current.move, current.state))
                current = current.parent
            return path[::-1]

        closed_set.add(current.state)

        for neighbor in get_neighbors(current):
            if neighbor.state in closed_set:
                continue
            heapq.heappush(open_set, neighbor)

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("-" * 9)

if __name__ == "__main__":
    # Example initial state (0 represents the blank space)
    initial_state = (
        1, 2, 3,
        0, 4, 6,
        7, 5, 8
    )
    
    print("Initial State:")
    print_board(initial_state)

    solution = solve_8_puzzle(initial_state)

    if solution:
        print(f"Solution found in {len(solution)} steps!\n")
        current_state = initial_state
        for step, (move, state) in enumerate(solution, 1):
            print(f"Step {step}: Move {move}")
            print_board(state)
    else:
        print("No solution exists for the given initial state.")