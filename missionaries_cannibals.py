# State is represented as (missionaries_left, cannibals_left, boat_side)
# Boat side: 1 means left, 0 means right

initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

def is_valid(state):
    m, c, b = state
    # check limits
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # check if missionaries are outnumbered on left side
    if m > 0 and m < c:
        return False
    # check if missionaries are outnumbered on right side
    m_right = 3 - m
    c_right = 3 - c
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_moves(state):
    m, c, b = state
    possible_states = []
    # (missionaries_in_boat, cannibals_in_boat)
    moves = [(1,0), (0,1), (1,1), (2,0), (0,2)]
    
    for move in moves:
        if b == 1: # boat is moving to the right
            new_state = (m - move[0], c - move[1], 0)
        else: # boat is moving to the left
            new_state = (m + move[0], c + move[1], 1)
            
        if is_valid(new_state):
            possible_states.append(new_state)
    return possible_states

def solve():
    queue = [[initial_state]]
    visited = []
    visited.append(initial_state)
    
    while queue:
        path = queue.pop(0)
        current = path[-1]
        
        if current == goal_state:
            return path
            
        for next_state in get_moves(current):
            if next_state not in visited:
                visited.append(next_state)
                new_path = list(path)
                new_path.append(next_state)
                queue.append(new_path)
    return None

ans = solve()
if ans:
    print("Steps to solve:")
    for step in ans:
        print(step)
else:
    print("No solution found")
