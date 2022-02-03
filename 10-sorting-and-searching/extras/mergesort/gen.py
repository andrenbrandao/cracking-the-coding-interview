import random


def gen(seed):
    random.seed(seed)
    n = 10 ** 7
    arr = [random.randint(1, 10 ** 5) for _ in range(n)]

    return arr
