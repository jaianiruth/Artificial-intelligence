"""8-Queens problem solver using backtracking."""

N = 8


def solve_n_queens(n=N):
    """Return a list of all solutions.
    Each solution is a list where index = row and value = column.
    """
    solutions = []
    placement = [0] * n          # placement[row] = column of the queen
    cols = set()                 # occupied columns
    diag1 = set()                # occupied (row - col) diagonals
    diag2 = set()                # occupied (row + col) anti-diagonals

    def place(row):
        if row == n:             # all queens placed
            solutions.append(placement[:])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue         # square is under attack
            # place the queen
            placement[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            place(row + 1)       # move on to the next row

            # backtrack: remove the queen
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    place(0)
    return solutions


def print_board(solution):
    """Print one solution as a chessboard (Q = queen, . = empty)."""
    n = len(solution)
    for row in range(n):
        print(" ".join("Q" if solution[row] == col else "." for col in range(n)))
    print()


if __name__ == "__main__":
    all_solutions = solve_n_queens(N)
    print(f"Total solutions for {N}-Queens: {len(all_solutions)}\n")

    print("First solution:\n")
    print_board(all_solutions[0])
