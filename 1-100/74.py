# Definition for singly-linked list.
from typing import List


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 23

    print(searchMatrix(matrix, target))


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if matrix == None or len(matrix) == 0:
        return False

    low = 0
    high = len(matrix) - 1

    index = -1

    while low <= high and low < len(matrix) and high < len(matrix):
        middle = int((low + high) / 2 + 0.5)

        if target > matrix[middle][0]:
            low = middle + 1
        elif target < matrix[middle][0]:
            high = middle - 1
        else:
            index = middle
            break

    if index == -1:
        index = high

    print(str(index)+ "--" + str(low) + "--" + str(high))

    low = 0
    high = len(matrix[0]) - 1

    num = -1

    while low <= high and low < len(matrix[0]) and high < len(matrix[0]):
        middle = int((low + high) / 2 + 0.5)

        print(middle)

        if target > matrix[index][middle]:
            low = middle + 1
        elif target < matrix[index][middle]:
            high = middle - 1
        else:
            num = middle
            break

    return num != -1


if __name__ == '__main__':
    main()
