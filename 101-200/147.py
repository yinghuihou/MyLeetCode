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
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(7)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g


    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    printList(insertionSortList(a))

def insertionSortList(head: ListNode) -> ListNode:
    if head == None:
        return None

    top = ListNode(0)
    top.next = head

    work = head.next
    head.next = None

    while work != None:
        p = work.next
        k = top
        while k != None and k.next != None and k.next.val < work.val:
            k = k.next
        work.next = k.next
        k.next = work
        work = p

    return top.next




if __name__ == '__main__':
    main()
