# Definition for singly-linked list.
from typing import List


def main():
    numList = [[0, 1, 0, 0],
               [1, 1, 1, 0],
               [0, 1, 0, 0],
               [1, 1, 0, 0]]

    print(islandPerimeter(numList))


def islandPerimeter(grid: List[List[int]]) -> int:
    if grid == None or len(grid) == 0:
        return 0

    result = 0
    if len(grid) == 1:
        for i in range(0, len(grid[0])):
            if grid[0][i] == 0:
                continue
            else:
                if i == 0 or i == len(grid[0]) - 1:
                    result += 3
                elif grid[0][i - 1] == 0 and grid[0][i + 1] == 0:
                    result += 4
                elif grid[0][i - 1] == 0 and grid[0][i + 1] != 0:
                    result += 3
                elif grid[0][i - 1] != 0 and grid[0][i + 1] == 0:
                    result += 3
                else:
                    result += 2

    for i in range(0, len(grid)):
        for k in range(0, len(grid[i])):
            if grid[i][k] == 0:
                continue
            else:
                if i - 1 in range(0, len(grid)) and grid[i - 1][k] == 0:
                    result += 1

                if i - 1 < 0:
                    result += 1

    return result


if __name__ == '__main__':
    main()
