import sys

n = int(sys.argv[1])

from gen import gen
from solution import radixsort

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    main = radixsort(input_data)
    print("Main:", main)
