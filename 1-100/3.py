# Definition for singly-linked list.


def main():
    str = 'd'
    print(lengthOfLongestSubstring(str))

def lengthOfLongestSubstring(s: str) -> int:

    if s == '':
        return 0

    if s != '' and s.strip() == '':
       return 1

    result = 0
    list = []

    for i in range(len(s)):
        if s[i] not in list:
            list.append(s[i])
        else:
            if len(list) > result:
                result = len(list)
            list = list[list.index(s[i]) + 1:]
            list.append(s[i])

    if len(list) > result:
        result = len(list)

    return result

if __name__ == '__main__':
    main()
