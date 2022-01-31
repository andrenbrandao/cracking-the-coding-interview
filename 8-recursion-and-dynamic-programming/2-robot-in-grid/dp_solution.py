"""
Problem:

8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.

Hints: #331, #360, #388

--

Questions:

- Is there always a valid solution? That is, the robot can always get to the bottom right?
No. Take care of this case.

- Is it safe to assume that it cannot walk through the walls of the grid?
Yes.

- Can we return any path? Does it make sense to try to find the shortest one?
I am going to assume any path is valid, since any path will have the same number of steps.

--
Algorithm:

[r,0,0,0,0]
[0,0,x,0,0]
[0,x,0,0,0]<
[0,0,0,0,0]
       ^

To reach the bottom right cell (r, c), the robot needs to be able to reach the cells
to the left (r, c-1) and move right or the cell above it (r-1, c) and move down.

That means that we can break this into subproblems. By removing a row or column,
we try to find if the robot can reach the new point (r, c). So, we recursively
try to see if a robot in the origin can reach this new point.

-- Optimizing it --

Notice that we are going through some cells more than one time.
Ex: (r-1, c-1) is reached when we go to (r-1,c) and (r, c-1). So, we could
mark it as reachable or not to prevent duplicate work.

"""


def robot_in_grid_points(grid):
    path = []
    height = len(grid)
    width = len(grid[0])

    def find_path(grid, row, col, path):
        if row == 0 and col == 0:
            path.append((0, 0))
            return True

        if not is_path(grid, row, col):
            return False

        if find_path(grid, row, col - 1, path) or find_path(grid, row - 1, col, path):
            path.append((row, col))
            return True

        return False

    def is_path(grid, row, col):
        if row < 0 or col < 0 or grid[row][col] == "x":
            return False

        return True

    find_path(grid, height - 1, width - 1, path)
    return path


def robot_in_grid_points_memo(grid):
    path = []
    height = len(grid)
    width = len(grid[0])
    memo = dict()

    def find_path(grid, row, col, path, memo):
        if row == 0 and col == 0:
            path.append((0, 0))
            return True

        if (row, col) in memo:
            return memo[(row, col)]

        if not is_path(grid, row, col):
            memo[(row, col)] = False
            return False

        if find_path(grid, row, col - 1, path, memo) or find_path(
            grid, row - 1, col, path, memo
        ):
            memo[(row, col)] = True
            path.append((row, col))
            return True

        memo[(row, col)] = False
        return False

    def is_path(grid, row, col):
        if row < 0 or col < 0 or grid[row][col] == "x":
            return False

        return True

    find_path(grid, height - 1, width - 1, path, memo)
    return path


def test(grid, expected_answer):
    answer = robot_in_grid_points_memo(grid)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test([["r"]], [(0, 0)])
    test(
        [
            ["r", "0", "0"],
            ["0", "0", "0"],
        ],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
    ),
    test(
        [
            ["r", "x", "0"],
            ["x", "0", "0"],
        ],
        [],
    )
    test(
        [
            ["r", "x", "0"],
            ["0", "x", "0"],
            ["0", "0", "0"],
        ],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    )
    test(
        [
            ["r", "x", "0"],
            ["0", "0", "0"],
            ["x", "0", "0"],
        ],
        [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],
    ),
    test(
        [
            ["r", "0", "0", "0", "0", "0", "0"],
            ["0", "x", "x", "x", "x", "x", "x"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "x", "x", "x", "x", "x", "x"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "x", "x", "x", "x", "x", "x"],
            ["0", "0", "0", "0", "0", "0", "x"],
            ["0", "0", "0", "0", "0", "0", "0"],
        ],
        [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (7, 1),
            (7, 2),
            (7, 3),
            (7, 4),
            (7, 5),
            (7, 6),
        ],
    )
    test(
        [
            ["r", "0", "0", "x", "0"],
            ["0", "0", "0", "x", "x"],
            ["x", "x", "0", "0", "0"],
            ["x", "x", "x", "x", "0"],
        ],
        [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4)],
    )
    print("All tests passed!")
