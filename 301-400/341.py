# Definition for singly-linked list.
import pickle


class NestedInteger:

    def __init__(self, list: [], value: int):
        self.integer = value
        self.list = list

    def isInteger(self) -> bool:
        return self.integer != None and self.list == None

    def getInteger(self) -> int:
        return self.integer

    def getList(self) -> []:
        return self.list


class NestedIterator:
    data = []

    def __init__(self, nestedList: [NestedInteger]):

        self.dfs(nestedList)
        self.index = 0

    def next(self) -> int:
        result = self.data[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.data)

    def dfs(self, nestedList: [NestedInteger]):
        for i in range(0, len(nestedList)):
            if nestedList[i].isInteger():
                self.data.append(nestedList[i].getInteger())
            else:
                self.dfs(nestedList[i].getList())


def main():
    a1 = NestedInteger(None, 1)
    a2 = NestedInteger(None, 3)
    a = NestedInteger([a1, a2], None)

    b = NestedInteger(None, 2)

    c1 = NestedInteger(None, 3)
    c2 = NestedInteger(None, 4)
    c3 = NestedInteger(None, 5)

    c = NestedInteger([c1, c2, c3], None)
    d = NestedInteger(None, 6)

    i = NestedIterator([a, b, c, d])
    v = []

    while i.hasNext():
        v.append(i.next())

    print(v)


if __name__ == '__main__':
    main()
