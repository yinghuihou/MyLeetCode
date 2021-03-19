import math
import time


def main():
    value = []

    for i in range(1000):
        result = findNumber(i)
        if sum(result) == i:
            value.append(i)
    print(value)


def findNumber(num: int):
    result = []

    if num == 0:
        result.append(0)
    elif num == 1:
        result.append(1)
    else:
        for k in range(1, num):
            if num % k == 0:
                result.append(k)
    return result


if __name__ == '__main__':
    main()
