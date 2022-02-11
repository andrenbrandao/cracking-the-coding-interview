"""
Problem:

3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Hints:#27, #59, #78

--
Algorithm

The default implementation of a Stack already has Push and Pop as operations in O(1) time.
Thus, the goal here is to implement the Min operation. How can we do this?

We have to somehow keep a list of the minimum values so that we can reach them really fast.
A Hashmap would not work because it won't be ordered with the same order the elements were added
to the stack.
A MinHeap would help, but the operations to remove the elements would be O(logn) time.

Another option is to use another stack to keep the minimum elements.

Let's look at an example:

Input: [5,2,3,6,1]

OriginalStack
[5,2,3,6,1] - the last element is on top

MinStack
[5,2,1]

Every time we push a new element, if it is less than or equal to the top
of the MinStack, we added there too. When MinStack is empty, we just add the element.
Also, when we pop an element, we check if the element is in the top of the MinStack,
if it is, we pop it there.

Now, when we want to check the minimum element, we just look at the top of the
MinStack.

--

How to test it?

Let's assume our input is a list of operations in a stack:
- Push
- Pop
- Min

Our return will be the minimum values we asked for. So we will check
if they are correct.

"""


class StackWithMin:
    def __init__(self) -> None:
        self.__stack = []
        self.__min_stack = []

    def push(self, val):
        self.__stack.append(val)

        if not self.__min_stack:
            self.__min_stack.append(val)
        elif val <= self.__min_stack[-1]:
            self.__min_stack.append(val)

    def pop(self):
        if not self.__stack:
            raise Exception("Stack is empty")
        if self.__stack[-1] == self.__min_stack[-1]:
            self.__min_stack.pop()

        return self.__stack.pop()

    def min(self):
        if not self.__stack:
            raise Exception("Stack is empty")
        return self.__min_stack[-1]


def query_stack(commands):
    stack = StackWithMin()

    result = []

    for command in commands:
        query = command.split()
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "min":
            min_value = stack.min()
            result.append(min_value)

    return result


def test(commands, expected_answer):
    answer = query_stack(commands)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(["push 5", "push 1", "push 2", "min", "pop", "min", "pop", "min"], [1, 1, 5])
    test(["push 5", "min", "push 6", "min", "push 2", "min"], [5, 5, 2])
    test(["push 5", "push 1", "push 3", "push 1", "min", "pop", "min"], [1, 1])
    test(["push -5", "min", "push 6", "push -6", "min"], [-5, -6])
    print("All tests passed!")
