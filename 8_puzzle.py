import heapq

class PuzzleState:
    def __init__(self, board, goal_board, moves=0, previous_state=None):
        self.board = board
        self.goal_board = goal_board
        self.moves = moves
        self.previous_state = previous_state
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def is_goal(self):
        return self.board == self.goal_board

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val != 0:
                    target_i = (val - 1) // 3
                    target_j = (val - 1) % 3
                    distance += abs(i - target_i) + abs(j - target_j)
        return distance

    def get_neighbors(self):
        neighbors = []
        i, j = self.blank_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_board = [row[:] for row in self.board]
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                neighbors.append(PuzzleState(new_board, self.goal_board, self.moves + 1, self))
                
        return neighbors

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

def solve_8_puzzle(initial_board, goal_board):
    initial_state = PuzzleState(initial_board, goal_board)
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)
    visited = set()

    while priority_queue:
        current_state = heapq.heappop(priority_queue)

        board_tuple = tuple(tuple(row) for row in current_state.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.previous_state
            return path[::-1]

        for neighbor in current_state.get_neighbors():
            heapq.heappush(priority_queue, neighbor)

    return None

if __name__ == "__main__":
    initial = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial State:")
    for row in initial: print(row)
    
    print("\nSolving...")
    path = solve_8_puzzle(initial, goal)
    
    if path:
        print(f"Solved in {len(path) - 1} moves!")
        for step, state in enumerate(path):
            print(f"\nStep {step}:")
            for row in state:
                print(row)
    else:
        print("No solution found.")
