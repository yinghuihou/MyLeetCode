# Definition for singly-linked list.
import sys

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
    b = ListNode(2)
    c = ListNode(4)
    d = ListNode(4)
    e = ListNode(4)
    f = ListNode(7)
    g = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # f.next = g


    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    printList(deleteDuplicates(a))

def deleteDuplicates(head: ListNode) -> ListNode:

    if head == None or head.next == None:
        return head

    top = ListNode(None)
    top.next = head
    left = top
    right = left.next

    while right != None and right.next!= None:

        if right.val != right.next.val:
            left = left.next
            right = right.next
        else:

            while right != None and right.next != None and right.val == right.next.val:
                right = right.next

            # 发现right和right后边的相同
            left.next = right.next
            right = left.next

    return top.next
if __name__ == '__main__':
    main()
