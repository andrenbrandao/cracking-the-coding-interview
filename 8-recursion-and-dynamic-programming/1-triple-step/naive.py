def naive_triple_step(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (
            naive_triple_step(n - 1)
            + naive_triple_step(n - 2)
            + naive_triple_step(n - 3)
        )
