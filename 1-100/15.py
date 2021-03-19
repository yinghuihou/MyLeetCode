# Definition for singly-linked list.
from typing import List


def main():
    numList = [-1, 0, 1, 2, -1, -4]
    # print(str(str1)[len(str(str1)):0:-1])
    # print(threeSum(numList, 0))
    print(quchong(threeSum(numList, 0)))


def threeSum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    numMap = {}
    length = len(nums)
    m = None
    a = None
    b = None
    c = None
    for i in range(0, length):
        if m != None and m == nums[i] and m <= 0:
            continue
        else:
            m = nums[i]

        if target - nums[i] not in numMap:
            numMap[target - nums[i]] = twoSum(nums, target - nums[i], i)
            for k in range(0, len(numMap[target - nums[i]])):
                if len(numMap[target - nums[i]][k]) == 2:
                    tmp = []
                    tmp.append(nums[i])
                    tmp.extend(numMap[target - nums[i]][k])
                    result.append(tmp)
    return result


def quchong(nums: List[List[int]]):
    result = {}
    for i in range(0, len(nums)):
        nums[i].sort()
        result[str(nums[i])] = nums[i]

    return list(result.values())


def twoSum(nums: List[int], target: int, index: int) -> List[List[int]]:
    result = []
    numMap = {}
    a = None
    b = None

    length = len(nums)
    for i in range(0, length):
        if i == index:
            continue

        if target - nums[i] in numMap:
            if a != None and b != None:
                # print("a:" + str(a) + "-- b:" + str(b) + "-- x:" + str(target - nums[i]) + "-- y:" + str(nums[i]))
                if a * b != (target - nums[i]) * nums[i]:
                    tmp = []
                    tmp.append(target - nums[i])
                    tmp.append(nums[i])
                    result.append(tmp)
                    a = target - nums[i]
                    b = nums[i]
            else:
                tmp = []
                tmp.append(target - nums[i])
                tmp.append(nums[i])
                result.append(tmp)
                a = target - nums[i]
                b = nums[i]

        numMap[nums[i]] = i
    print("targrt:" + str(target) + "---result:" + str(result))
    return result


if __name__ == '__main__':
    main()
