import sys

n = int(sys.argv[1])

from solution import check_balanced, check_balanced_1
from gen import gen

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    model = check_balanced_1(input_data)
    print("Model:", model)

    main = check_balanced(input_data)
    print("Main:", main)

    if model != main:
        print("ERROR!")
        break
