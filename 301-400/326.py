# Definition for singly-linked list.
from queue import Queue
import math


def main():
    s = "[3,4,5,1,3,null,1]"

    print(isPowerOfThree(18))


def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False

    result = False
    index = 1
    while index < n:
        index = index * 3
        if index == n:
            result = True

    return result


if __name__ == '__main__':
    main()
