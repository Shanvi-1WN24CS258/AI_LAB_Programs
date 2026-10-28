
import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def misplaced_tiles(state, goal):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal[i]
    )


def manhattan_distance(state, goal):
    distance = 0

    for num in range(1, 9):
        curr = state.index(num)
        target = goal.index(num)

        r1, c1 = divmod(curr, 3)
        r2, c2 = divmod(target, 3)

        distance += abs(r1 - r2) + abs(c1 - c2)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[idx] = (
                new_state[idx], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start, goal, heuristic):
    open_list = [
        Node(start, None, 0, heuristic(start, goal))
    ]
    visited = set()
    best_g = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)

        if current.state in visited:
            continue

        if current.state == goal:
            path = []

            while current:
                path.append(current.state)
                current = current.parent

            path.reverse()

            for step, state in enumerate(path):
                print("Step", step)
                for i in range(0, 9, 3):
                    print(state[i:i + 3])
                print()

            print("Total moves:", len(path) - 1)
            return

        visited.add(current.state)

        for neighbor in get_neighbors(current.state):
            new_g = current.g + 1

            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                h = heuristic(neighbor, goal)

                heapq.heappush(
                    open_list,
                    Node(neighbor, current, new_g, h)
                )

    print("No solution found")


start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

print("CASE 1: Misplaced Tiles")
a_star(start, goal, misplaced_tiles)

print("CASE 2: Manhattan Distance")
a_star(start, goal, manhattan_distance)
