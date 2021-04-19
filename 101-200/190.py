# Definition for singly-linked list.

def main():
    print(reverseBits("00000010100101000001111010011100"))


def reverseBits(n: int) -> int:
    s = ""
    s += str(n)[::-1]
    s += '0' * 32

    return int(s[:32], 2)


if __name__ == '__main__':
    main()
