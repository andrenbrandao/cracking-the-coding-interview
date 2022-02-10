# Exercise 11.1

Mistake: Find the mistake(s) in the following code:

```c
unsigned int i;
for (i = 100; i >= 0; --i)
  printf("%d\n", i);
```

Hints: #257, #299, #362

## Solution

The goal of the code is to print numbers 100 to 0. So, by looking at it quickly, it looks right. But, the most interesting part is the use of an `unsigned int`.

In this case, unsigned integers range from 0 to (2^32)-1. When the loop gets to i=0 and subtracts 1, the new value of `i` will be (2^32)-1 and we will have an infinite loop.

To fix it, we either have to use a signed integer or we have to stop the loop before. One way to fix the loop is:

```c
unsigned int i;
for (i = 101; i > 0; --i)
  printf("%d\n", i - 1);
```

Notice that I assumed the goal was to print numbers from 100 to 0. The book assumed it was from 100 to 1, so it gave a different solution.

PS: The book's solution states that the `printf` statement should use `%u` in place of `%d`. Nice catch for all C programmers out there. :)
