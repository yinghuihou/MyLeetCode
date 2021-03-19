# Definition for singly-linked list.
from typing import List

def main():
    numList = [2, 7, 14, 15,20]
    # print(str(str1)[len(str(str1)):0:-1])
    print(twoSum(numList, 22))



def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    numMap = {}
    length = len(nums)
    for i in range(0, length):
        if target - nums[i] in numMap:
            result.append(numMap[target - nums[i]])
            result.append(i)
            return result
        numMap[nums[i]] = i


if __name__ == '__main__':
    main()
