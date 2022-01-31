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

Example of a grid where 'x's are off limit cells.

[r,0,0,0,0]
[0,0,x,0,0]
[0,x,0,0,0]
[0,0,0,0,0]

The easiest approach is to use DFS and try to walk through all the possible cells
until we get to the bottom right.

We have to 'find the path', that means that we have to return the path as soon
as we reach the end.

To store the path, we might want to create a sequence of right-down steps:
'rrrdddr'.

"""


"""
DFS SOLUTION

This was a very trick one.

In the beginning I was returning the path after each
recursive call, but this was leading to append even wrong paths to the result.

[r, 0, 0]
[0, x, x]
[0, 0, 0]

It happened because let's say we have a grid like the one above. The algorithm
would do "rr" and could not go down. By going to the last position, if we do
path = find_path(path + 'r') we would then be keeping the wrong paths, getting a
result of 'rrddrr' which is wrong.

The trick here is to only store the final path at the end. If we keep returning
this value from our calls, we will be mixing right and wrong paths.
"""


def robot_in_grid_strings(grid):
    finalPath = ""

    def find_path(grid, robot_height, robot_width, path):
        nonlocal finalPath
        width_max_pos = len(grid[0]) - 1
        height_max_pos = len(grid) - 1

        foundPath = False
        if robot_height == height_max_pos and robot_width == width_max_pos:
            finalPath = path
            return True

        if (
            robot_width + 1 <= width_max_pos
            and grid[robot_height][robot_width + 1] != "x"
        ):
            foundPath = find_path(grid, robot_height, robot_width + 1, path + "r")

        # every time we return from a recursive call, we have to check if we found the end
        # so that it prevents the recursive calls from following other paths
        if foundPath:
            return True

        if (
            robot_height + 1 <= height_max_pos
            and grid[robot_height + 1][robot_width] != "x"
        ):
            foundPath = find_path(grid, robot_height + 1, robot_width, path + "d")

        return foundPath

    find_path(grid, 0, 0, "")
    return finalPath


"""
DFS SOLUTION

This is a modification of the last solution to use a list of points and compare
the result to our model.

Notice that the path will be in reversed order.
"""


def robot_in_grid_points(grid):
    path = []

    def find_path(grid, robot_height, robot_width, path):
        width_max_pos = len(grid[0]) - 1
        height_max_pos = len(grid) - 1

        foundPath = False
        if robot_height == height_max_pos and robot_width == width_max_pos:
            path.append((robot_height, robot_width))
            return True

        if (
            robot_height + 1 <= height_max_pos
            and grid[robot_height + 1][robot_width] != "x"
        ):
            foundPath = find_path(grid, robot_height + 1, robot_width, path)

        if foundPath:
            path.append((robot_height, robot_width))
            return True

        if (
            robot_width + 1 <= width_max_pos
            and grid[robot_height][robot_width + 1] != "x"
        ):
            foundPath = find_path(grid, robot_height, robot_width + 1, path)

        if foundPath:
            path.append((robot_height, robot_width))
            return True
        else:
            return False

    find_path(grid, 0, 0, path)
    return path[::-1]


def test(grid, expected_answer, method):
    answer = method(grid)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test([["r"]], "", robot_in_grid_strings)
    test([["r"]], [(0, 0)], robot_in_grid_points)
    test(
        [
            ["r", "0", "0"],
            ["0", "0", "0"],
        ],
        "rrd",
        robot_in_grid_strings,
    ),
    test(
        [
            ["r", "x", "0"],
            ["x", "0", "0"],
        ],
        "",
        robot_in_grid_strings,
    ),
    test(
        [
            ["r", "x", "0"],
            ["x", "0", "0"],
        ],
        [],
        robot_in_grid_points,
    )
    test(
        [
            ["r", "0", "0"],
            ["0", "0", "0"],
        ],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        robot_in_grid_points,
    )
    test(
        [
            ["r", "x", "0"],
            ["0", "x", "0"],
            ["0", "0", "0"],
        ],
        "ddrr",
        robot_in_grid_strings,
    )
    test(
        [
            ["r", "x", "0"],
            ["0", "0", "0"],
            ["x", "0", "0"],
        ],
        "drrd",
        robot_in_grid_strings,
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
        "ddddddrrrrrdr",
        robot_in_grid_strings,
    )
    test(
        [
            ["r", "0", "0", "x", "0"],
            ["0", "0", "0", "x", "x"],
            ["x", "x", "0", "0", "0"],
            ["x", "x", "x", "x", "0"],
        ],
        "rrddrrd",
        robot_in_grid_strings,
    )
    print("All tests passed!")
