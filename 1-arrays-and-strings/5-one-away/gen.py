import sys
import random
import string


def gen(n):
    random.seed(n)

    x_len = random.randint(0, 3)
    y_len = random.randint(0, 3)

    x = "".join(random.choice(string.ascii_lowercase) for i in range(x_len))
    y = "".join(random.choice(string.ascii_lowercase) for i in range(y_len))

    return x, y
