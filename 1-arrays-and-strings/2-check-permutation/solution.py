"""
Problem:

1.2 Given two strings, write a method to decide if one is a permutation of the other.

--
Questions:

- Are the inputs always valid strings?
- Is the comparison case sensitive?
- Should we consider spaces as valid characters?

--
Algorithm:

*1st option*
Count the letters on the first string and store it in a hashmap. Then,
count the ones on the second string. Then, go through each letter on the
first hashmap and check if the count is the same.

The problem with this approach is that we could have a string with less letters
than the other, but with the same count. Ex: [aaabb, aaabbcc]

To mitigate this, we could check if both hashmaps have the same amount of keys.

Time Complexity: O(n)

*2nd option*
Use an array to store the characters. This would work if we were using ASCII,
but if we consider UTF-8, we can end up with a very large array.

*3rd option*
Sort the string and compare them.

Time Complexity: O(nlgn)

*Final Choice*
Let's go with the first approach.

"""

from collections import Counter


def is_permutation(str1, str2):
    letter_count1 = Counter(str1)
    letter_count2 = Counter(str2)

    if len(letter_count1) != len(letter_count2):
        return False

    for key in letter_count1:
        if letter_count2.get(key) != letter_count1[key]:
            return False

    return True


def test(str1, str2, expected_answer):
    answer = is_permutation(str1, str2)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test("", "", True)
    test("", "a", False)
    test("a", "", False)
    test("aabb", "aabb", True)
    test("aabb", "aabbcc", False)
    test("aabbcc", "aabb", False)
    test("bbaacc", "ccaabb", True)
    test("🚀📘🎯", "🚀🎯📘", True)
    print("All tests passed!")
