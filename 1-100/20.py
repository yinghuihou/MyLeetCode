# Definition for singly-linked list.

def main():
    s = "([)]"
    s1 = "{[]}"
    isValid(s1)


def isValid(s: str) -> bool:
    if s == None:
        return False

    if s.strip() == "":
        return True

    result = []
    for i in range(0, len(s)):

        if len(result) == 0:
            result.append(s[i])
            continue

        left = result[len(result) - 1]
        if isRight(left, s[i]):
            result.pop()

        else:
            result.append(s[i])

    return (len(result) == 0)


def isRight(s1, s2):
    if s1 == "(" and s2 == ")":
        return True
    if s1 == "[" and s2 == "]":
        return True
    if s1 == "{" and s2 == "}":
        return True
    return False


if __name__ == '__main__':
    main()
