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
    b = ListNode(7)
    c = ListNode(6)
    d = ListNode(4)
    e = ListNode(4)
    f = ListNode(7)
    g = ListNode(8)
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
    printList(partition(a,5))

def partition(head: ListNode, x: int) -> ListNode:
    low = ListNode(0)
    high = ListNode(0)
    low_top = low
    high_top = high

    while head != None:
        if head.val < x:
            low.next = head
            head = head.next
            low = low.next
            low.next = None
        else:
            high.next = head
            head = head.next
            high = high.next
            high.next = None

    low.next = high_top.next
    return low_top.next






if __name__ == '__main__':
    main()
