import random


def gen(seed):
    random.seed(seed)
    n = 10 ** 5
    arr = [random.randint(1, 10 ** 9) for _ in range(n)]

    return arr
