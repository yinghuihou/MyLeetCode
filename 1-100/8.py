# Definition for singly-linked list.

def main():
    str = '   3333333333333333333333333333333333333'
    print(myAtoi(str))


def myAtoi(str: str) -> int:
    if str == None or str == '' or str.strip() == '':
        return 0

    result = str.lstrip()
    number = 0
    if not result[0].isdigit() and result[0] != '-' and result[0] != '+' and not result[1].isdigit():
        return 0

    if result[0].isdigit():
        for i in range(0, len(result)):
            if result[i].isdigit():
                number = number * 10 + int(result[i])

            else:
                break
    elif result[0] == '-':
        for i in range(1, len(result)):
            if result[i].isdigit():
                number = number * 10 + int(result[i])
            else:
                break
        number = - number
    elif result[0] == '+':
        for i in range(1, len(result)):
            if result[i].isdigit():
                number = number * 10 + int(result[i])
            else:
                break

    if number >= 2**31:
        number = 2**31-1

    if number <= -2**31:
        number = -2**31
    return number


if __name__ == '__main__':
    main()
