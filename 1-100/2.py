# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(l: ListNode):
    while l != None:
        print(l.val)
        l = l.next


def main():
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    a.next = b
    b.next = c

    a1 = ListNode(5)
    b1 = ListNode(6)
    c1 = ListNode(4)
    a1.next = b1
    b1.next = c1

    #printList(a)
    addTwoNumbers(a,a1)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    r1 = 0
    r2 = 0
    i = 0
    j = 0

    result = ListNode(0)
    head = result

    while l1 != None:
        r1 += l1.val * pow(10,i)
        l1 = l1.next
        i += 1

    while l2 != None:
        r2 += l2.val * pow(10,j)
        l2 = l2.next
        j += 1

    number = r1 + r2
    lenth = len(str(number))

    for i in range(lenth):
        l = ListNode(number % 10)
        result.next = l
        result = result.next
        number = number // 10

    return head.next

if __name__ == '__main__':
    main()
