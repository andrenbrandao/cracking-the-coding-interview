import sys
import time

from gen import gen
from radixsort.solution import radixsort
from countingsort.solution import countingsort

n = int(sys.argv[1])

avg1 = []
avg2 = []

for i in range(n):
    print()
    print(f"Test #{str(i)}")

    input_data = gen(i)
    print("Input:", input_data)

    start = time.time()
    radix = radixsort(input_data)
    print("Radix Sort:", radix)
    time1 = time.time() - start
    avg1.append(time1)

    start = time.time()
    count = countingsort(input_data)
    print("Counting Sort:", count)
    time2 = time.time() - start
    avg2.append(time2)

    if radix != count:
        print("ERROR!")
        break

    print(f"Execution 1: {time1}")
    print(f"Execution 2: {time2}")

print(f"Avg Radix Sort: {sum(avg1)/len(avg1)}")
print(f"Avg Counting Sort: {sum(avg2)/len(avg2)}")
