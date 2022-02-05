"""
Problem:

10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.

Hints: #117, #182, #263, #342

--

Questions:

- Should the strings also be sorted alphabetically or is the method
only responsible to group the strings by anagrams?
- Can we assume the strings have only ASCII characters?
- Should we consider uppercase letters as the same? Ex: DOG and god.

--

Algorithm:

A word is an anagram of another if they contain the same number of each letter.
Ex: dog, god

If strings are of different length, they are not anagrams of each other.

-- Option 1 --
If we sort the characters in every string, we can then sort the array and
the anagrams will be grouped together.

"""


def group_anagrams(words):
    sorted_words = sorted(words, key=lambda x: sorted(list(x)))
    return sorted_words


def test(words, expected_answer):
    answer = group_anagrams(words)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(["dog", "hi", "god"], ["dog", "god", "hi"])
    test(
        ["john", "doe", "abra", "braa", "nohj", "hey"],
        ["abra", "braa", "doe", "hey", "john", "nohj"],
    )
    test(["dog", "hey", "dddo", "bbbog", "god"], ["bbbog", "dddo", "dog", "god", "hey"])
    print("All tests passed!")
