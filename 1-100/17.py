# Definition for singly-linked list.
from typing import List
from functools import reduce


def main():
    numList = [-1, 0, 1, 2, -1, -4]
    # print(str(str1)[len(str(str1)):0:-1])
    # print(threeSum(numList, 0))
    print(letterCombinations("5"))


def letterCombinations(digits: str) -> List[str]:
    numberMap = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    result = []

    if digits == None or len(digits) == 0:
        return result

    for i in range(0, len(digits)):
        result.append(numberMap[digits[i]])
    return reduce(sum, result)


def sum(list1: List[str], list2: List[str]):
    result = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            result.append(list1[i] + list2[j])

    return result


if __name__ == '__main__':
    main()
