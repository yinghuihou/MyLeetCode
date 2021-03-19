# Definition for singly-linked list.
from typing import List


def main():
    print(generateParenthesis(4))


def generateParenthesis(n: int):
    result = []
    kuo = ""

    if n == 1:
        result.append("()")
    elif n == 2:
        result.append("()()")
        result.append("(())")
    else:
        lastList = generateParenthesis(n - 1)

        for i in range(0, len(lastList)):
            s = lastList[i]
            print(s)
            for k in range(0,len(s)):
                if s[k] == "(":
                    tmp = s[:k + 1] + "()" + s[k +1:]
                    if tmp not in result:
                        result.append(tmp)
        for i in range(0,n):
            kuo = kuo + "()"

        result.append(kuo)
    print(len(result))
    return result


if __name__ == '__main__':
    main()
