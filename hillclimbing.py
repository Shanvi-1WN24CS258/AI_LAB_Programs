from itertools import combinations

def cost(state):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
    
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing():
    current = [3, 1, 2, 0]

    while True:
        current_cost = cost(current)
        print("Current state:", current, "Cost:", current_cost)

        if current_cost == 0:
            print("Goal state reached!")
            return

        best = current
        best_cost = current_cost

      
        for i, j in combinations(range(4), 2):
            neighbour = current.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]

            neighbour_cost = cost(neighbour)

            print("Neighbour:", neighbour, "Cost:", neighbour_cost)

            if neighbour_cost < best_cost:
                best = neighbour
                best_cost = neighbour_cost

       
        if best == current:
            print("Local minimum reached. Stopping.")
            return

        current = best


hill_climbing()