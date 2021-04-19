# Definition for singly-linked list.
from typing import List


def main():
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


def removeDuplicates(nums: List[int]) -> int:
    if nums == None:
        return None
    if len(nums) <= 1:
        return len(nums)

    result = 1
    same = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] != same:
            nums[result] = nums[i]
            result += 1
            same = nums[i]
        i += 1

    return result


if __name__ == '__main__':
    main()
