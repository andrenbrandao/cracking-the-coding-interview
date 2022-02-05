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

We could somehow count the letters of each string and group them by this
"blueprint". But how do we create this?

Can we count the number of letters in each string and them hash it?
The problem with hashing is that we can have collisions, therefore we can get
strings with different counts and same hash.

If we assume we only have letters a-z, we could lowercase all strings,
then, use ord(letter) - ord('a') to create a unique identifier for the count
of letters and sort by this identifier.

Ex:
dog: 3+14+6 = 23
god: 6+14+3 = 23
hi:  7+8    = 15

Sorting the elements above, we will get dog and god next to each other.

-- REVIEWING THE ALGORITHM ABOVE --

What if we have the following case:
3+3+14 = 20
6+14 = 20

We will have two different words, grouped together.
Therefore, this is not a good solution.

ex: "dog", "hey", "dddo", "bbbog", "god"
will not group 'dog' and 'god' together.
"""


class Word:
    def __init__(self, word):
        self.original_word = word
        self.word = word.lower()
        self.identifier = self.create_word_identifier(self.word)

    def create_word_identifier(self, word):
        identifier = 0

        for letter in word:
            identifier += ord(letter) - ord("a")

        return identifier

    def __lt__(self, other):
        return self.identifier < other.identifier

    def __eq__(self, other):
        return self.identifier == other.identifier


def group_anagrams(words):
    identified_words = [Word(word) for word in words]
    grouped_words = sorted(identified_words)
    return [word.original_word for word in grouped_words]


def test(words, expected_answer):
    answer = group_anagrams(words)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(["dog", "hi", "god"], ["hi", "dog", "god"])
    test(
        ["john", "doe", "abra", "braa", "nohj", "hey"],
        ["abra", "braa", "doe", "hey", "john", "nohj"],
    )
    test(
        ["dog", "hey", "dddo", "bbbog", "god"], ["bbbog", "dddo", "dog", "god", "hey"]
    )  # this should fail!
    print("All tests passed!")
