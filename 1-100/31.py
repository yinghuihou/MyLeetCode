from typing import List


def main():
    words = [1, 3, 2,1,3,2]

    nextPermutation(words)

    print(words)


def nextPermutation(nums: List[int]) -> None:
    if nums == None or len(nums) == 0:
        return

    find = False
    tmp = -1
    for i in range(1, len(nums) + 1):
        index = nums[-i]

        for j in range(i + 1, len(nums) + 1):
            if nums[-j] < index:
                tmp = j
                find = True
                index = nums[-i]
                nums[-i] = nums[-j]
                nums[-j] = index
                break

        if find:
            break
    print(tmp)

    if not find:
        nums.reverse()
    else:
        tmpList = []
        tmpList2 = []
        for i in range(0, len(nums)):
            if i < len(nums) - tmp + 1:
                tmpList.append(nums[i])
            else:
                tmpList2.append(nums[i])

        tmpList2.sort()
        nums.clear()
        nums.extend(tmpList)
        nums.extend(tmpList2)


if __name__ == '__main__':
    main()
