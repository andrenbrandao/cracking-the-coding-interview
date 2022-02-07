"""
Bucket sort works by placing the elements in buckets and then
sorting each bucket.

For integers, this can end up solving the problem in linear time if
we are able to put one element in each bucket.

[4,3,5,6,2]

Buckets
0:
1:
2: 2
3: 3
4: 4
5: 5
6: 6

Going through all elements in the bucket: [2,3,4,5,6]

Now, let's do this for floating numbers.

[0.85, 0.33, 0.45, 0.50, 0.42]

Let's break these numbers into buckets by their first digit in the mantissa.

0:
1:
2:
3: 0.33
4: 0.45, 0.42
5: 0.50
6:
7:
8: 0.85
9:

We have to sort the elements in the bucket. If we use Insertion Sort,
which is O(n²), we might have a O(n²) algorithm in the worst case,
when all elements endup in the same bucket.
We can use Merge Sort or other O(nlgn) algorithm to improve it.

After sorting it, go through the buckets and recreate an array:

[0.33, 0.42, 0.45, 0.50, 0.85]

Time Complexity: O(n+k) on average, O(n²) or O(nlogn) on worst case.
Space Complexity: O(n+k)
"""


def bucketsort(arr):
    buckets = [[] for _ in range(10)]

    for num in arr:
        digit = int(num * 10)
        buckets[digit].append(num)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        for val in bucket:
            result.append(val)

    return result


def test(input_data, expected_answer):
    answer = bucketsort(input_data)

    if answer != expected_answer:
        raise Exception(
            f"Wrong answer {answer}. Expected answer was {expected_answer}."
        )


if __name__ == "__main__":
    test([0.85, 0.33, 0.45, 0.50, 0.42], [0.33, 0.42, 0.45, 0.50, 0.85])
    print("All tests passed!")
