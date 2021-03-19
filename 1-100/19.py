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
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    # d.next = e

    a1 = ListNode(5)
    b1 = ListNode(6)
    c1 = ListNode(4)
    a1.next = b1
    b1.next = c1

    #printList(a)
    addTwoNumbers(a,1)


def addTwoNumbers(head: ListNode, n: int) -> ListNode:

    x = head
    y = head
    j = 0
    len = 0
    while y != None:
        y = y.next
        len += 1
        j += 1
        if j > n and y != None:
            x = x.next

    if n == len :
        return head.next
    else:
        k = x.next
        x.next = k.next
        k = None
        return head

if __name__ == '__main__':
    main()
