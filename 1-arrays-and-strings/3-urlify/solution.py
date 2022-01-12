"""
Problem:

1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE

Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

Hints: #53, #118

--

Algorithm:

- Go from right to left on the string searching for spaces. Start from the length - 1.
- When we find a space, shift all the characters to the right by 2 places.
- Increment the length of the string by 2.
- On the empty space, add the %20 characters
- Repeat until we have read all characters of the string.

Time Complexity: O(n²) because we have to shift all characters to the right
for every new space.

Optimal Algorithm:

             i   j
"Mr John Smith    "
- j is the index where we will start storing the characters
- i is the pointer we will use to read from right to left

- Count the number of spaces and define a new index where we will start moving the characters
- Go from right to left.
    - If it is a character, write it to str[index]. Decrement the index.
    - If it is a space, we have to write to the index in reverse order. Decrement the index by 3.

Time Complexity: O(n)

"""


def shift_characters_right(array_str, start_pos, end_pos):
    for position in range(end_pos, start_pos - 1, -1):
        array_str[position + 2] = array_str[position]


def urlify_space(array_str, start_pos):
    array_str[start_pos] = "%"
    array_str[start_pos + 1] = "2"
    array_str[start_pos + 2] = "0"


def urlify(str1, length):
    current_length = length
    array_str = list(str1)

    for position in range(length - 1, -1, -1):
        if array_str[position] == " ":
            shift_characters_right(array_str, position + 1, current_length - 1)
            urlify_space(array_str, position)
            current_length += 2

    return "".join(array_str)


def urlify_optimal(str1, length):
    array_str = list(str1)
    space_count = 0

    for i in range(length):
        if array_str[i] == " ":
            space_count += 1

    index = length + space_count * 2
    for position in range(length - 1, -1, -1):
        if array_str[position] == " ":
            array_str[index - 1] = "0"
            array_str[index - 2] = "2"
            array_str[index - 3] = "%"
            index -= 3

        else:
            array_str[index - 1] = array_str[position]
            index -= 1

    return "".join(array_str)


def test(str1, length, expected_answer):
    answer = urlify_optimal(str1, length)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test("Mr John Smith    ", 13, "Mr%20John%20Smith")
    test("Mr John                    ", 13, "Mr%20John%20%20%20%20%20%20")
    test(" Mr John Smith      ", 14, "%20Mr%20John%20Smith")
    print("All tests passed!")
