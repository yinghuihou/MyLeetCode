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
    #e.next = f
    #f.next = g


    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    printList(reorderList(a))

def reorderList(head: ListNode):
    if head == None:
        return None
    work = head
    num = 0
    while work != None:
        work = work.next
        num += 1

    if num % 2 == 0:
        k = int(num / 2)
    else:
        k = int(num / 2) + 1
    i = 1
    iwork = head
    while i < k:
        iwork = iwork.next
        i += 1

    p = iwork.next
    iwork.next = None

    nodes = []
    while p != None:
        q = p.next
        p.next = None
        nodes.append(p)
        p = q

    m = head
    nodes.reverse()
    while m != None and len(nodes) != 0:
        n = m.next
        j = nodes.pop(0)
        j.next = n
        m.next = j
        m = n
    return head





if __name__ == '__main__':
    main()
