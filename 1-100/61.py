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
    printList(rotateRight(a, 7))


def rotateRight(head: ListNode, k: int) -> ListNode:
    end = head
    work = head
    go = False
    len = 0
    while end != None:
        len += 1
        if end.next != None:
            end = end.next
        else:
            break

    if len - k >= 0:
        m = len - k
    else:
        m = len - (k % len)

    if m == 0:
        return head
    else:
        end.next = head
        while m > 0:
            m -= 1
            head = head.next
            if go:
                work = work.next
            go = True
        work.next = None
        return head


if __name__ == '__main__':
    main()
