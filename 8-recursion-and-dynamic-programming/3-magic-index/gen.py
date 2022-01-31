from random import randint
import random


def gen(seed):
    random.seed(seed)
    n = randint(1, 10 ** 5)
    arr_set = set([random.randint(-100, 10 ** 5) for _ in range(n)])

    return sorted(list(arr_set))
