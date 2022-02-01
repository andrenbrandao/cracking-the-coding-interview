import sys

n = int(sys.argv[1])

from gen import gen
from solution import mergesort_less_memory, mergesort

for i in range(1):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    main = mergesort_less_memory(input_data)
    print("Main:", main)
