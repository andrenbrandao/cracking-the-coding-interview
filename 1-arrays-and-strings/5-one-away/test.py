import sys
import os

n = int(sys.argv[1])

from solution import one_away, one_away_dp
from gen import gen

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    model = one_away_dp(*input_data)
    print("Model:", model)

    main = one_away(*input_data)
    print("Main:", main)

    if model != main:
        print("ERROR!")
        break
