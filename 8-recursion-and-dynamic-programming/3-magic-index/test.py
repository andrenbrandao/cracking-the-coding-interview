import sys

n = int(sys.argv[1])

from gen import gen
from solution import find_magic_index, find_magic_index_binary_search

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    model = find_magic_index(input_data)
    print("Model:", model)

    main = find_magic_index_binary_search(input_data)
    print("Main:", main)

    if model != main:
        print("ERROR!")
        break
