def dls(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),  
        (1, 0), 
        (0, -1),
        (0, 1)   
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in path:
                result = dls(
                    new_state,
                    goal,
                    depth - 1,
                    path + [new_state]
                )

                if result:
                    return result

    return None


def iddfs(start, goal):
    depth = 0

    while True:
        result = dls(start, goal, depth, [start])

        if result:
            return result

        depth += 1



start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)


goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = iddfs(start, goal)

print("Solution:")

for state in solution:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()