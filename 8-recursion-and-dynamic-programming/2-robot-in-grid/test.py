import sys

n = int(sys.argv[1])

from model import getPath
from dp_solution import robot_in_grid_points
from gen import gen

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    model = getPath(input_data)
    print("Model:", model)

    main = robot_in_grid_points(input_data)
    print("Main:", main)

    if model != main:
        print("ERROR!")
        break
