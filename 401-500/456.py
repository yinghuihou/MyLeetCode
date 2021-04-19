# Definition for singly-linked list.
import pickle
from typing import List
import sys


def find132pattern(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    length = len(nums)

    low = nums[0]

    for i in range(1, length):
        for k in range(length - 1, i, -1):
            if low < nums[k] and nums[k] < nums[i]:
                return True
        low = min(low, nums[i])
    return False


def find132pattern2(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    length = len(nums)

    minList = [sys.maxsize] * length

    # 找到每一个数值左边部分的最小值，并一一对应
    for i in range(1, length):
        minList[i] = min(minList[i - 1], nums[i - 1])

    stack = []

    for i in range(length - 1, -1, -1):

        numsk = -sys.maxsize

        while len(stack) != 0 and nums[i] > stack[-1]:
            numsk = stack.pop()

        if numsk > minList[i]:
            return True
        stack.append(nums[i])

    return False

def main():
    nums = [-1, 3, 2, -2]
    print(find132pattern(nums))


if __name__ == '__main__':
    main()
