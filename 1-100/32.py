# Definition for singly-linked list.

def main():
    s = "()"
    s1 = ")()())"
    isValid(s)


def isValid(s: str) -> int:
    if s == None or s.strip() == "":
        return 0

    result = []
    resultIndex = []
    resultIndex.append(-1)
    for i in range(0, len(s)):

        if len(result) == 0:
            result.append(s[i])
            resultIndex.append(i)
            continue

        left = result[len(result) - 1]
        if isRight(left, s[i]):
            result.pop()
            resultIndex.pop()

        else:
            result.append(s[i])
            resultIndex.append(i)

    resultIndex.append(len(s))

    print(resultIndex)
    index = 0
    for i in range(1, len(resultIndex)):
        if resultIndex[i] - resultIndex[i - 1] > index:
            index = resultIndex[i] - resultIndex[i - 1]
    print(index - 1)


def isRight(s1, s2):
    if s1 == "(" and s2 == ")":
        return True
    return False


if __name__ == '__main__':
    main()
