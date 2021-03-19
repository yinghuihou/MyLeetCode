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
    printList(reverseBetween(a,1,7))

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:

    if head == None or head.next == None:
        return head
    x = m
    y = n
    top = ListNode(0)
    top.next = head
    pre = top
    end = head
    m = m-1

    while m != 0:
        pre = pre.next
        end = end.next
        m -= 1

    k = y - x + 1
    tmp = end
    while k > 1:
        tmp = tmp.next
        k -= 1

    #tmp.next即为尾部链表的头结点
    m = tmp.next
    tmp.next = None
    tmp = m

    pre.next = None
    result = end
    while end != None:
        index = end.next
        end.next = pre.next
        pre.next = end
        end = index

    result.next = tmp
    return top.next

if __name__ == '__main__':
    main()
