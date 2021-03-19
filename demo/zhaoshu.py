import math
import time


def main():
    result = []

    start = time.time()
    for i in range(9999999):
        if findNumber(i) == i:
            result.append(i)
    end = time.time()
    print(end - start)
    print(result)

    start = time.time()
    print(findNumber2(9999999))
    end = time.time()
    print(end - start)


def findNumber(number: int):
    sNumber = str(number)
    length = len(sNumber)

    result = 0
    for i in sNumber:
        result += math.pow(int(i), length)
    return result


def findNumber2(max: int):
    tmp = 0
    number_list = []

    k = 1

    for index in range(max):
        sNumber = str(index)
        length = len(sNumber)

        if index < 10:
            number_list.append(index)
        else:
            if k == 11:
                k = 1

            if k == 1:
                tmp = 0
                for i in sNumber[:length - 1]:
                    tmp += math.pow(int(i), length)

                if tmp + math.pow(int(sNumber[-1]), length) == index:
                    number_list.append(index)
                k += 1
            else:
                if tmp + math.pow(int(sNumber[-1]), length) == index:
                    number_list.append(index)
                k += 1
    print(number_list)


if __name__ == '__main__':
    main()
