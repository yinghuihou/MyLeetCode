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
    b = ListNode(3)
    c = ListNode(4)
    a.next = b
    b.next = c

    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    addTwoNumbers(a, a1)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    x = l1
    y = l2
    head = ListNode(0)
    result = head

    while x != None and y != None:
        if x.val <= y.val:
            head.next = x
            x = x.next
        else:
            head.next = y
            y = y.next
        head = head.next
    if x == None:
        head.next = y
    else:
        head.next = x

    printList(result.next)

if __name__ == '__main__':
    main()
