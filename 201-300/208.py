# Definition for singly-linked list.

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.endPoint = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for s in word:
            if s not in current_node.children:
                # 查询的字符不在当前节点的孩子里
                child = TreeNode(s)
                current_node.children[s] = child
                current_node = child
            else:
                current_node = current_node.children[s]

        current_node.endPoint = True

    def search(self, word: str) -> bool:

        current_node = self.root
        result = True
        for s in word:
            if s not in current_node.children:
                # 查询的字符不在当前节点的孩子里
                result = False
                break
            else:
                current_node = current_node.children[s]

        if not current_node.endPoint:
            result = False

        return result

    def startsWith(self, prefix: str) -> bool:

        current_node = self.root
        result = True
        for s in prefix:
            if s not in current_node.children:
                # 查询的字符不在当前节点的孩子里
                result = False
                break
            else:
                current_node = current_node.children[s]

        return result


def main():
    obj = Trie()
    print(obj.insert("apple"))
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))

    print(obj.insert("app"))
    print(obj.search("app"))

if __name__ == '__main__':
    main()
