# Definition for singly-linked list.


result_map = {}


def main():
    print(isScramble("great", "tegar"))


def isScramble(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    if hashNum(s1) != hashNum(s2):
        return False

    # 两个长度相等且内部字符相等
    len1 = len(s1)

    if len1 <= 3:
        return True

    if s1 in result_map and s2 in result_map[s1]:
        return result_map[s1][s2]

    for i in range(1, len1):
        s1_left = s1[0:i]
        s1_right = s1[i:]

        s2_left = s2[0:i]
        s2_right = s2[i:]

        # 进行递归
        if (isScramble(s1_left, s2_left) and isScramble(s1_right, s2_right)) or (
                isScramble(s1_left, s2[len1 - i:]) and isScramble(s1_right, s2[0:len1 - i])):
            result_map[s1] = {s2: True}
            return True
    result_map[s1] = {s2: False}
    return False


def hashNum(s: str):
    num = 0
    for i in range(len(s)):
        num += ord(s[i]) - ord("a")
    return num


if __name__ == '__main__':
    main()
