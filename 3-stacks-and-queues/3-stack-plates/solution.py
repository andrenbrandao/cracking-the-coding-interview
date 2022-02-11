"""
Problem:

3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this.

SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.

Hints: #64, #87

--
Algorithm

Let's create a class SetOfStacks that will receive the threshold as a parameter in it's constructor.
The class will will have a list of stacks.
When the last stack reaches the length of the threshold, we add another stack to the list.
Also, when popping, we always pop from the last stack. After popping it, if the stack is empty, we remove it
from the list.

--
How can we test it?

We can have the following inputs
- push 5
- pop
- print

When we call print, we will receive a list of the elements in the stack. This is what
we will use to check if the stack is correctly implemented.

We can first create a NaiveImplementation of the stack and test if the push, pop and
print operations are working correctly. After that, we can change our implementation
to use a set of stacks while making sure the tests pass.
"""

# First iteration
class NaiveStack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        return self.__stack.pop()

    def to_list(self):
        return self.__stack[:]


# Second iteration
class SetOfStacks:
    def __init__(self, threshold=10) -> None:
        self.__threshold = threshold
        self.__set_of_stacks = []

    def push(self, val):
        if not self.__set_of_stacks:
            self.__set_of_stacks.append([val])
            return

        if len(self.__set_of_stacks[-1]) < self.__threshold:
            self.__set_of_stacks[-1].append(val)
        else:
            self.__set_of_stacks.append([val])

    def pop(self):
        if not self.__set_of_stacks:
            raise Exception("Stack is empty")

        value = self.__set_of_stacks[-1].pop()
        if not self.__set_of_stacks[-1]:
            self.__set_of_stacks.pop()

        return value

    def to_list(self):
        result = []

        for stack in self.__set_of_stacks:
            for val in stack:
                result.append(val)
        return result

    def number_of_stacks(self):
        return len(self.__set_of_stacks)


def query_stack(commands, threshold):
    stack = SetOfStacks(threshold)

    result = []

    for command in commands:
        query = command.split()
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "print":
            result.append(stack.to_list())
        elif query[0] == "number_of_stacks":
            result.append(stack.number_of_stacks())
        else:
            raise Exception("Invalid command")

    return result


def test(commands, threshold, expected_answer):
    answer = query_stack(commands, threshold)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(
        [
            "push 5",
            "push 2",
            "print",
            "pop",
            "print",
        ],
        10,
        [[5, 2], [5]],
    )
    test(
        [
            "push 5",
            "push 2",
            "push 1",
            "push 5",
            "push 4",
            "push 5",
            "push 3",
            "push 5",
            "push 2",
            "push 5",
            "print",
        ],
        2,
        [[5, 2, 1, 5, 4, 5, 3, 5, 2, 5]],
    )
    test(
        [
            "push 5",
            "push 2",
            "print",
            "pop",
            "print",
            "pop",
            "print",
        ],
        2,
        [[5, 2], [5], []],
    )
    test(["push 5", "number_of_stacks", "pop", "number_of_stacks"], 2, [1, 0])
    test(
        [
            "push 5",
            "push 2",
            "push 3",
            "number_of_stacks",
            "push 4",
            "number_of_stacks",
            "push 5",
            "number_of_stacks",
            "pop",
            "number_of_stacks",
        ],
        2,
        [2, 2, 3, 2],
    )
    print("All tests passed!")
