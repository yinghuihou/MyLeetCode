# Definition for singly-linked list.
from typing import List


def main():
    str = "aaa"
    p = "a*a"
    print(isMatch(str, p))



def isMatch(s: str, p: str) -> bool:
    i = 0
    k = 0
    while i < len(s) and k < len(p):
        if s[i] == p[k]:
            i += 1
            k += 1
        elif p[k] == '.':
            i += 1
            k += 1
        elif p[k] == '*':
            if p[k - 1] == ".":
                if k == len(p) - 1:
                    return True
                else:
                    return False
            elif p[k - 1] == s[i]:
                if i == len(s) - 1 and k == len(p) - 1:
                    return True
                else:
                    i += 1
            else:
                k += 1
        else:
            if p[k + 1] == '*':
                k += 2
            else:
                return False

    if k >= len(p) - 1:
        if (k == len(p) - 1 and (i == len(s) - 1)):
            return True
        elif (k == len(p) and i == len(s)):
            return True
        else:
            return False
    elif p[k] == "*" and s.endswith(p[k + 1:]):
        return True
    else:
        return False



if __name__ == '__main__':
    main()
