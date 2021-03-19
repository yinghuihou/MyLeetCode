# Definition for singly-linked list.
from typing import List


def main():
    str = [1, 2, 3, 4, 5]
    print(maxArea(str))


def maxArea(height: List[int]) -> int:
    if height == None or len(height) < 2:
        return None

    i = 0
    k = len(height) - 1
    result = getArea(height[i], height[k], i, k)
    while i < k:
        if height[i] <= height[k]:
            if height[i + 1] > height[i]:
                if result < getArea(height[i + 1], height[k], i + 1, k):
                    result = getArea(height[i + 1], height[k], i + 1, k)
                else:
                    i += 1
            else:
                i += 1
        else:
            if height[k - 1] > height[k]:
                if result < getArea(height[i], height[k - 1], i, k - 1):
                    result = getArea(height[i], height[k - 1], i, k - 1)
                else:
                    k -= 1
            else:
                k -= 1
    return result


def getArea(x: int, y: int, x1: int, y1: int):
    if x <= y:
        m = x
    else:
        m = y
    return m * (y1 - x1)


if __name__ == '__main__':
    main()
