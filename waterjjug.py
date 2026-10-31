from collections import deque

def water_jug_bfs(cap1, cap2, target):
    if target > max(cap1, cap2):
        return None
    if target % gcd(cap1, cap2) != 0:
        return None

    start = (0, 0)
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path + [(a, b)]

        next_states = [
            (cap1, b),        # fill jug1
            (a, cap2),        # fill jug2
            (0, b),           # empty jug1
            (a, 0),           # empty jug2
            (max(0, a - (cap2 - b)), min(cap2, a + b)),  # pour jug1 -> jug2
            (min(cap1, a + b), max(0, b - (cap1 - a))),  # pour jug2 -> jug1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(a, b)]))

    return None


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    cap1, cap2, target = 4, 3, 2  # example: 4L and 3L jugs, measure 2L

    result = water_jug_bfs(cap1, cap2, target)

    if result:
        print(f"Solution found in {len(result) - 1} steps:")
        for i, (a, b) in enumerate(result):
            print(f"Step {i}: Jug1 = {a}L, Jug2 = {b}L")
    else:
        print("No solution exists.")