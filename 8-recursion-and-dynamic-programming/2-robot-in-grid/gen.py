from random import randint
import random


def gen(seed):
    random.seed(seed)
    width = randint(1, 100)
    height = randint(1, 100)

    grid = [[0 for _ in range(width)] for _ in range(height)]
    grid[0][0] = "r"

    for i in range(height):
        for j in range(width):
            if i == 0 and j == 0:
                continue

            grid[i][j] = random.choices(["0", "x"], [80, 20])

    grid[height - 1][width - 1] = "0"
    print(grid)
    return grid


gen(10)
