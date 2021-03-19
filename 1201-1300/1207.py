# Definition for singly-linked list.
from typing import List


def main():
    numList = [1,2,2,1,1,2,3]
    # print(str(str1)[len(str(str1)):0:-1])
    print(uniqueOccurrences(numList))


def uniqueOccurrences(nums: List[int]) -> bool:

    if nums == None or len(nums) == 0:
        return True

    result = []
    result2 = []
    numMap = {}
    length = len(nums)
    for i in range(0, length):
        if nums[i] in numMap:
            numMap[nums[i]] += 1
        else:
            numMap[nums[i]] = 1

    for i in numMap.values():
        result.append(i)
        if i not in result2:
            result2.append(i)

    return len(result) == len(result2)


if __name__ == '__main__':
    main()
