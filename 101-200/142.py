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
    f.next = a


    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1

    # printList(a)
    print(detectCycle(a).val)


def detectCycle(head : ListNode):
    if head == None:
        return None

    top = head
    end = head
    has = False
    while(top != None and end != None and end.next != None):
        top = top.next
        end = end.next.next
        if top == end:
            has = True
            break;
    if has:
        end = head
        while end != None and end.next != None:
            if end == top:
                break
            end = end.next
            top = top.next

        return end
    else:
        return None




if __name__ == '__main__':
    main()
