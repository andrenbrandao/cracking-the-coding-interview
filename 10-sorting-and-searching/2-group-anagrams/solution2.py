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

-- Option 2 --
We can group the strings by anagram. If we sort the characters in the string,
we can store them in a hashmap by this given "original sorted string".

{
    'dog': ['dog', 'god'],
    'hey': ['hey']
}

At the end, we go through all the keys of the hashmap and add the elements
to the returned array.

"""


def group_anagrams(words):
    hashmap = dict()

    for word in words:
        if sorted_word(word) in hashmap:
            hashmap[sorted_word(word)].append(word)
        else:
            hashmap[sorted_word(word)] = [word]

    result = []
    for key in hashmap:
        for word in hashmap[key]:
            result.append(word)

    return result


def sorted_word(word):
    list_word = list(word)
    sorted_word = sorted(list_word)
    return "".join(sorted_word)


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
        ["john", "nohj", "doe", "abra", "braa", "hey"],
    )
    test(["dog", "hey", "dddo", "bbbog", "god"], ["dog", "god", "hey", "dddo", "bbbog"])
    print("All tests passed!")
