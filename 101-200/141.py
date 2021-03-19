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
    a1.next = b1
    b1.next = c1

    # printList(a)
    print(hasCycle(a))

def hasCycle(head : ListNode):
    top = head
    end = head
    while(top != None and end != None and end.next != None):
        top = top.next
        end = end.next.next
        if top == end:
            return True

    return False

if __name__ == '__main__':
    main()
