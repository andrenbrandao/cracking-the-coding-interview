"""
Problem:

Gerate a list of primes up to a integer number N.

--

Algorithm:

More info: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

- Create an array up to N to indicate which numbers are prime. 0 and 1 should be false. The rest is true.
- Start with 2 and multiply it by itself until N, marking the numbers as not prime.
- Find the next element that was not removed and do the same.
- Repeat until we cannot get a next prime element.

"""

import math


def sieve_of_erastothenes(number):
    is_prime_flags = [True for _ in range(number + 1)]
    is_prime_flags[0], is_prime_flags[1] = False, False

    prime = 2

    while prime <= math.sqrt(number):
        cross_multiples(prime, is_prime_flags)
        prime = find_next_prime(prime, is_prime_flags)

    return [i for i, val in enumerate(is_prime_flags) if val]


def cross_multiples(prime, is_prime_flags):
    for i in range(prime * prime, len(is_prime_flags), prime):
        is_prime_flags[i] = False


def find_next_prime(prime, is_prime_flags):
    for i in range(prime + 1, len(is_prime_flags)):
        if is_prime_flags[i]:
            return i

    return prime


def test(number, expected_answer):
    answer = sieve_of_erastothenes(number)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(3, [2, 3])
    test(5, [2, 3, 5])
    test(11, [2, 3, 5, 7, 11])
    test(30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    print("All tests passed!")
