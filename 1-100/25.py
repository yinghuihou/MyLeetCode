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
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(7)
    g = ListNode(8)
    a.next = b
    b.next = c
    # c.next = d
    # d.next = e
    # e.next = f
    # f.next = g

    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    printList(reverseKGroup(a, 4))


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    top = ListNode(0)
    i = 0
    work = head
    m = head
    result = top

    swap = False

    while head != None:
        head = head.next
        i += 1
        if i >= 2:
            m = m.next

        if i == k:
            i = 0
            m.next = None
            swapPairs(work)
            swap = True
            work.next = head
            top.next = m
            top = work
            work = head
            m = work

    if not swap:
        return work
    else:
        return result.next


def swapPairs(head: ListNode) -> ListNode:
    top = ListNode(0)

    while head != None:
        p = head.next
        head.next = top.next
        top.next = head
        head = p

    return top.next


if __name__ == '__main__':
    main()
