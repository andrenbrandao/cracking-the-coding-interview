"""
Problem:

8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.

Hints: #152, #178, #217, #237, #262, #359

--

Algorithm:

--Naive--

We could break the N steps into subproblems.

     [0, 1, 2, 3, 4..n] ...n steps
 -3 /      -2 | -1  \
  n-3        n-2     n-1

This would create a tree with all possibilities. Time complexity is O(3^n)

--Memoization--
Let's consider each step as a node in a DAG.

0    1    2    3    n-1   n
o -> o -> o -> o ... o -> o

The number of ways to get to N is the number of ways to get from 0 to N.
To get from N-1 to N, there is only one way, with one step.
From N-2, it can jump to N-1 or directly to N.
From N-3, it can jump to N-2, N-1 or directly to N.
Then, the rest are subproblems.

f(n-1) = f(n)
f(n-2) = f(n) + f(n-1)
f(n-3) = f(n-2) + f(n-1) + f(n)

"""


# DAG Solution
def triple_step(n):
    memo = (n + 1) * [1]

    for i in reversed(range(n)):
        if i + 1 == n:
            memo[i] = memo[i + 1]
        elif i + 2 == n:
            memo[i] = memo[i + 2] + memo[i + 1]
        else:
            memo[i] = memo[i + 3] + memo[i + 2] + memo[i + 1]

    return memo[0]


# Another way it to use memoization with the recursive solution
def memo_triple_step(n):
    def _memo_triple_step(n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n]:
            return memo[n]
        else:
            memo[n] = (
                _memo_triple_step(n - 1, memo)
                + _memo_triple_step(n - 2, memo)
                + _memo_triple_step(n - 3, memo)
            )

            return memo[n]

    memo = (n + 1) * [None]
    return _memo_triple_step(n, memo)


def test(number, expected_answer):
    answer = triple_step(number)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(1, 1)
    test(2, 2)
    test(3, 4)
    test(9, 149)
    test(8, 81)
    test(6, 24)
    print("All tests passed!")
