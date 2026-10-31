def solve_n_queens(n=8):
    solutions = []
    board = [-1] * n  # board[row] = column of queen in that row

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def print_board(solution, n=8):
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()


if __name__ == "__main__":
    solutions = solve_n_queens(8)
    print(f"Total solutions for 8-Queens: {len(solutions)}\n")

    # Print the first solution as an example
    if solutions:
        print("Example solution:")
        print_board(solutions[0])