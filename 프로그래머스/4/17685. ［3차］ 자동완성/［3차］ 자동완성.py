class Tree:
    def __init__(self):
        self.root = Node('root')
        
    def putString(self, string):
        curr = self.root
        
        for s in string:
            child = curr.getChild(s)
            if child is None:
                child = Node(s, curr)
                curr.child.append(child)
            curr.count += 1
            curr = child
        curr.count += 1
            
    def printT(self, node=None, depth=0):
        if node is None: node = self.root
        
        print("\t"*depth, f"{node.value}({node.count})")
        
        for child in node.child:
            self.printT(child, depth+1)
            
    def getString(self, string):
        curr = self.root
        answer = 0
        
        for s in string:
            if curr.count <= 1:
                return answer
            curr = curr.getChild(s)
            answer += 1
        return answer


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.child = list()
        self.count = 0
        
    def getChild(self, value):
        for c in self.child:
            if c.value == value:
                return c
        return None
        
    


def solution(words):
    answer = 0
    tree = Tree()
    for word in words:
        tree.putString(word)
    for word in words:
        answer += tree.getString(word)
    return answer