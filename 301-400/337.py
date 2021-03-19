# Definition for singly-linked list.
from queue import Queue
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def main():
    s = "[3,4,5,1,3,null,1]"
    root = TreeNode(0)
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)
    root5 = TreeNode(5)
    root6 = TreeNode(6)

    root.left = root1
    root.right = root2

    root1.left = root3
    root1.right = root4

    root2.left = root5
    rob(root)


def rob(root: TreeNode) -> int:
    list = Queue(maxsize=0)
    result = []
    list.put(root)

    money = 0
    money2 = 0

    while list.qsize() != 0:
        size = list.qsize()
        tmp = 0
        for i in range(0, size):
            node = list.get()
            tmp += node.val

            if node.left != None:
                list.put(node.left)

            if node.right != None:
                list.put(node.right)
        result.append(tmp)

    for i in range(0,len(result)):
        if i%2 == 0:
            money += result[i]
        else:
            money2 += result[i]

    return (max(money,money2))


if __name__ == '__main__':
    main()
