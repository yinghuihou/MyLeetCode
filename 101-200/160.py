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
    a1.next = d
    b1.next = c1


    print(getIntersectionNode(a, a1))


def getIntersectionNode(headA, headB):
    if headA == None or headB == None:
        return None

    workA = headA
    workB = headB
    lenA = 0
    lenB = 0
    m = 0

    maxA = False
    maxB = False

    while workA != None:
        lenA += 1
        workA = workA.next

    while workB != None:
        lenB += 1
        workB = workB.next

    if lenA >= lenB:
        maxA = True
        m = lenA - lenB
    else:
        maxB = True
        m = lenB - lenA

    workA = headA
    workB = headB
    if maxA:
        while workA != None and m > 0:
            workA = workA.next
            m -= 1
    else:
        while workB != None and m > 0:
            workB = workB.next
            m -= 1


    while workA != None and workB != None:
        if workA == workB:
            return workA.val
        else:
            workA = workA.next
            workB = workB.next

    return None


if __name__ == '__main__':
    main()
