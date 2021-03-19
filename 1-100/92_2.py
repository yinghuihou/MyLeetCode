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
    f = ListNode(6)
    g = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    d1 = ListNode(6)
    a1.next = b1
    b1.next = c1
    c1.next = d1

    # printList(a)
    printList(reverseBetween(a, 2, 4))


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if head == None:
        return None

    top = ListNode(0)
    top.next = head

    pre = top
    after = top
    len = 0
    while after.next != None and len < left:
        pre = after
        after = after.next
        len += 1

    while len < right and after.next != None:
        tmp = pre.next

        pre.next = after.next
        after.next = after.next.next
        pre.next.next = tmp
        len += 1

    return top.next


if __name__ == '__main__':
    main()
