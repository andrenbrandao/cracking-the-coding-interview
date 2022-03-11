"""
Problem:

3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

Hints: #98, #174

--
Algorithm

-- Pushing elements
Push 1, Push 2, Push 3

Stack1
[1, 2, 3]

Stack2
[]

-- Popping
Pop

Stack1
[]

Stack2
[3, 2, 1] -> pop from stack 2

--
We are going to have two stacks.

Push:
Always push to the first stack.

Pop:
Case 1 - Second stack is empty:
If first stack is also empty, raise Exception.
We pop all from the first and move them to
the second stack. Then, pop from the second.

Case 2 - Second stack has elements:
Pop elements from the second stack

Peek:
Case 1 - Second stack is empty:
Pop all elements from the first and move to the second stack.
Then, read from the top element of the second.

Case 2 - Second stack has elements:
Read the top element of the second stack.

"""


class MyQueue:
    def __init__(self) -> None:
        self._first_stack = []
        self._second_stack = []

    def push(self, value):
        self._first_stack.append(value)

    def pop(self):
        if self._second_stack:
            return self._second_stack.pop()

        if not self._first_stack:
            raise Exception("Queue is empty!")

        while self._first_stack:
            self._second_stack.append(self._first_stack.pop())

        return self._second_stack.pop()

    def peek(self):
        if self._second_stack:
            return self._second_stack[-1]

        if not self._first_stack:
            raise Exception("Queue is empty!")

        while self._first_stack:
            self._second_stack.append(self._first_stack.pop())

        return self._second_stack[-1]


# We receive commands such as 'push 4', 'pop'.
def query_queue(commands):
    queue = MyQueue()
    result = []

    for command in commands:
        action = command.split()
        if action[0] == "push":
            value = action[1]
            queue.push(int(value))
        elif action[0] == "pop":
            result.append(queue.pop())
        elif action[0] == "peek":
            result.append(queue.peek())

    return result


def test(commands, expected_answer):
    answer = query_queue(commands)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(["push 4", "pop"], [4])
    test(["push 1", "push 2", "push 3", "pop", "pop", "pop"], [1, 2, 3])
    test(
        ["push 1", "push 2", "pop", "push 3", "pop", "push 4", "pop", "pop"],
        [1, 2, 3, 4],
    )
    test(["push 1", "push 2", "peek", "pop", "pop"], [1, 1, 2])
    print("All tests passed!")
