"""
Problem:

3.1 Three in One: Describe how you could use a single array to implement three stacks.

Hints: #2, #12, #38, #58


--

*1st Option*

We could divide an array into three parts. For each part, store the number of elements
to not allow it to overflow into the other parts.

Let's create the following commands to operate over the three stacks:

- 0 push 10
- 1 push 20
- 2 push 30
- 0 pop
- 0 push 40
- 0 push 50

The first value is the reference to the stack. The second is the command: push, pop.
The third is the value that will be added.

The query_stacks method should return the final representation of the stacks.

"""


class Stack:
    def __init__(self, size=120):
        self.array = [0] * size
        self.length = [0, 0, 0]
        self.start = [0, size // 3, (size // 3) * 2]
        self.max_stack_size = size // 3

    def push(self, stack_number, value):
        if self.length[stack_number] >= self.max_stack_size:
            raise Exception("Stack is full!")

        self.array[self.start[stack_number] + self.length[stack_number]] = value
        self.length[stack_number] += 1

    def pop(self, stack_number):
        if self.length[stack_number] == 0:
            raise Exception("Stack is empty!")

        value = self.array[self.start[stack_number] + self.length[stack_number]]
        self.length[stack_number] -= 1
        return value

    def to_array(self):
        first_stack = self.array[self.start[0] : self.length[0]]
        second_stack = self.array[self.start[1] : self.start[1] + self.length[1]]
        third_stack = self.array[self.start[2] : self.start[2] + self.length[2]]

        return [first_stack, second_stack, third_stack]


def query_stacks(commands):
    stack = Stack()

    for command in commands:
        stack_number, operation, *value = command.split(" ")
        stack_number = int(stack_number)

        if operation == "push":
            stack.push(stack_number, int(value[0]))
        elif operation == "pop":
            stack.pop(stack_number)
        else:
            raise Exception("Wrong Command!")

    return stack.to_array()


def test(commands, expected_answer):
    answer = query_stacks(commands)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(
        ["0 push 10", "1 push 20", "2 push 30", "0 pop", "0 push 40", "0 push 50"],
        [[40, 50], [20], [30]],
    )
    print("All tests passed!")
