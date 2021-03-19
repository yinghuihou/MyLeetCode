# Definition for singly-linked list.


def main():
    str = 'abc'
    print(convert(str, 2))
    print(len(str))


def convert(s: str, numRows: int) -> str:
    if s is None or s.strip() == "":
        return s

    if len(s) == numRows :
        return s

    result = []
    for i in range(numRows):
        k = (((numRows - 1) * 2) - 1) - i * 2
        if i == numRows - 1:
            k = (((numRows - 1) * 2) - 1)
        if i == 0 or i == numRows - 1:
            m = i
            while m < len(s):
                print(s[m])
                result.append(s[m])
                m += (k + 1)
        else:
            m = i
            while m < len(s):
                result.append(s[m])
                if m + k + 1 < len(s):
                    result.append(s[m + k + 1])
                m += (numRows * 2 - 2)

    return "".join(result)


if __name__ == '__main__':
    main()
