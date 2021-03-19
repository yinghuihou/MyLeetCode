# Definition for singly-linked list.
from typing import List


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
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    a1 = ListNode(1)
    b1 = ListNode(3)
    c1 = ListNode(4)
    a1.next = b1
    b1.next = c1

    a2 = ListNode(2)
    b2 = ListNode(6)
    c2 = ListNode(3)
    a2.next = b2
    #b2.next = c2
    # printList(a)

    lists = []
    lists.append(a)
    lists.append(a1)
    lists.append(a2)

    printList(mergeKLists(lists))


def mergeKLists(lists: List[ListNode]) -> ListNode:
    if len(lists) < 1:
        return None
    elif len(lists) < 2:
        return lists[0]

    m = len(lists) // 2

    left = mergeKLists(lists[:m])
    right = mergeKLists(lists[m:])

    return  addTwoNumbers(left,right)

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None
    if l1 == None:
        return l2
    if l2 == None:
        return l1

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

    #printList(result.next)
    return result.next


if __name__ == '__main__':
    main()
