def solve(numheads, numlegs):
    # Let x be the number of chickens and y be the number of rabbits
    # x + y = numheads
    # 2x + 4y = numlegs
    # Solving the system of equations:
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x, y

# Example Usage
chickens, rabbits = solve(35, 94)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
