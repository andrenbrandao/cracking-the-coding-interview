"""
Problem:

1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE

pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Hints:#23, #97, #130

-- Algorithm:

The Edit Distance Problem calculates how many changes there are between two strings.

pale
bake

Given two strings, we can either match a character, replace, insert, or remove.

  p a l e
p 0 1 2 3
l 1 1 1 2
e 2 2 2 1

We could break it into subproblems.

Given two strings x[0,...,i] and y[0,...,j], the last column of the strings
will either be a match, mismatch, insert or deletion.

x[0,...,i-1] + x[i] -> match or mismatch
y[0,...,j-1] + y[j]

x[0,...,i-1] + x[i]
y[0,...,j]          -> insertion

x[0,...,i]
y[0,...,j-1] + y[j] -> deletion

Mismatch, deletion and insertion have a cost of 1.

So the ED(i,j) = min {
  ED(i-1, j-1) + diff(x[i], y[j]), where diff = 0 if match and diff = 1 if mismatch
  ED(i-1, j) + 1,
  ED(i, j-1) + 1
}

Base Case:
ED(i, 0) = i
ED(0, j) = j

Since the tree would have tree child nodes, this recursive solution would be O(3^len(s)).
Below, let's look for a tabular approach.

  __p a l e
_ 0 1 2 3 4 -> from empty string to pale, the edit distance increases
p 1 0 1 2 3
l 2 1 1 1 2
e 3 2 2 2 1

We can then create a matrix. Being the increasing size of the string X
in the first row and the size of the string Y in the first column.

Time Complexity: O(n*m)


--
The book's solution states an algorithm that is O(k) where k is the length
of the shortest string.

So, let's look at how to do this. When comparing to strings, we may have
the following cases:

-- 1st case
pale
ple

We could compare each character and when a mismatch is found, we skip one character
of the longest string. That way, we can keep comparing the next characters.
Ex:
 i
pale
 j
ple

i and j are different, so do i+1 and keep comparing them. If they mismatch again, return False.

-- 2nd case
ple
pale

This is the same case as the one above. So we might compare always the longest string
with the shortest.

-- 3rd case
pale
pake

Here, they have the same length, so we can just compare them directly and count
the mismatches.
"""


def one_away(first, second):
    if abs(len(first) - len(second)) >= 2:
        return False

    if len(first) > len(second):
        longest = first
        shortest = second
    else:
        longest = second
        shortest = first

    if len(first) == len(second):
        count = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                count += 1
            if count > 1:
                return False

    else:
        i = 0
        j = 0
        count = 0

        while i < len(longest) and j < len(shortest):
            if longest[i] != shortest[j]:
                count += 1
                j -= 1

            if count > 1:
                return False

            i += 1
            j += 1

    return True


def one_away_dp(first, second):
    edit_distance = [[0 for _ in range(len(first) + 1)] for _ in range(len(second) + 1)]

    for i in range(len(first) + 1):
        edit_distance[0][i] = i

    for i in range(len(second) + 1):
        edit_distance[i][0] = i

    for i in range(1, len(second) + 1):
        for j in range(1, len(first) + 1):
            diff = 0 if first[j - 1] == second[i - 1] else 1
            edit_distance[i][j] = min(
                edit_distance[i - 1][j - 1] + diff,
                edit_distance[i - 1][j] + 1,
                edit_distance[i][j - 1] + 1,
            )

    return edit_distance[-1][-1] <= 1


def test(first, second, expected_answer):
    answer = one_away(first, second)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test("pale", "ple", True)
    test("pales", "pale", True)
    test("pale", "bale", True)
    test("pale", "bake", False)
    test("pale", "pale", True)
    test("", "", True)
    test("a", "", True)
    test("d", "xm", False)
    print("All tests passed!")
