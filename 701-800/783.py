# Definition for singly-linked list.
from typing import List
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(1)
    d = TreeNode(3)
    e = TreeNode(6)

    a.left = b
    a.right = e

    b.left = c
    b.right = d

    minDiffInBST(a)

def minDiffInBST(root: TreeNode) -> int:
    result = []
    num = sys.maxsize

    if root == None:
        return None

    bianli(root, result)

    for i in range(len(result) - 1):
        if result[i+1] - result[i] < num:
            num = result[i+1] - result[i]
    print(num)

def bianli(root: TreeNode, result: List):
    if root.left is not None:
        bianli(root.left, result)
    result.append(root.val)

    if root.right is not None:
        bianli(root.right,result)


if __name__ == '__main__':
    main()
