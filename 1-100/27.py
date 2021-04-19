# Definition for singly-linked list.
from typing import List


def main():
    print(removeElement([0], 0))


def removeElement(nums: List[int], val: int) -> int:
    if nums == None:
        return None
    if len(nums) < 1 or (len(nums) == 1 and len(0) == val):
        return 0

    result = 0
    same = val
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[result] = nums[i]
            result += 1
        i += 1

    return result


if __name__ == '__main__':
    main()
