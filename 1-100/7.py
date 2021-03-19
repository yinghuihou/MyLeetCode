# Definition for singly-linked list.


def main():
    str1 = -123
    #print(str(str1)[len(str(str1)):0:-1])
    print(lengthOfLongestSubstring(str1))



def lengthOfLongestSubstring(x: int) -> int:

    if x < 0:
        result = int(str(x)[len(str(x)):0:-1])
    else:
        result = int(str(x)[::-1])

    if result > 2 ** 31 - 1 or result < -(2 ** 31):
        result = 0
    if x < 0:
        return -result
    return result


if __name__ == '__main__':
    main()
