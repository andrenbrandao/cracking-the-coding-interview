import sys
import os

n = int(sys.argv[1])

from naive import naive_triple_step
from solution import triple_step
from gen import gen

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen()
    print("Input:", input_data)

    model = naive_triple_step(input_data)
    print("Model:", model)

    main = triple_step(input_data)
    print("Main:", main)

    if model != main:
        print("ERROR!")
        break
