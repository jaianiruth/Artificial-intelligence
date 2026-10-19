"""Water Jug Problem solver using Breadth-First Search (BFS)."""

from collections import deque
from math import gcd


def water_jug(cap_x, cap_y, target):
    """Return the shortest list of (x, y, action) states reaching the target,
    or None if the target cannot be measured."""
    # A solution exists only if target <= max(cap) and target is a multiple of gcd
    if target > max(cap_x, cap_y) or target % gcd(cap_x, cap_y) != 0:
        return None

    start = (0, 0)
    parent = {start: (None, "Start with both jugs empty")}
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:          # goal reached
            path = []
            state = (x, y)
            while state is not None:
                prev, action = parent[state]
                path.append((state[0], state[1], action))
                state = prev
            return path[::-1]

        pour_xy = min(x, cap_y - y)             # amount that moves X -> Y
        pour_yx = min(y, cap_x - x)             # amount that moves Y -> X
        moves = [
            ((cap_x, y), f"Fill Jug X ({cap_x}L)"),
            ((x, cap_y), f"Fill Jug Y ({cap_y}L)"),
            ((0, y), "Empty Jug X"),
            ((x, 0), "Empty Jug Y"),
            ((x - pour_xy, y + pour_xy), "Pour Jug X into Jug Y"),
            ((x + pour_yx, y - pour_yx), "Pour Jug Y into Jug X"),
        ]
        for new_state, action in moves:
            if new_state not in parent:
                parent[new_state] = ((x, y), action)
                queue.append(new_state)

    return None


def print_solution(cap_x, cap_y, target):
    print(f"Jug X = {cap_x}L, Jug Y = {cap_y}L, Target = {target}L\n")
    path = water_jug(cap_x, cap_y, target)
    if path is None:
        print("No solution possible.")
        return
    print(f"{'Step':<5}{'Jug X':<7}{'Jug Y':<7}Action")
    print("-" * 45)
    for i, (x, y, action) in enumerate(path):
        print(f"{i:<5}{x:<7}{y:<7}{action}")
    print(f"\nSolved in {len(path) - 1} steps.")


if __name__ == "__main__":
    print_solution(4, 3, 2)
