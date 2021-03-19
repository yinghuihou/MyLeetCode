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
    a.next = b
    b.next = c
    #c.next = d

    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    printList(swapPairs(a))


def swapPairs(head: ListNode) -> ListNode:
    top = ListNode(0)
    top.next = head
    result = top

    i = top.next

    while i != None:
        j = i.next
        if j == None:
            break
        i.next = j.next
        j.next = i
        top.next = j
        top = i


        i = top.next

    return result.next

if __name__ == '__main__':
    main()
