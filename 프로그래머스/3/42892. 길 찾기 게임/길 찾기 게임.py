import sys
sys.setrecursionlimit(10**4)

class Node:
    def __init__(self, index, x, y, left = None, right = None, parent = None):
        self.index = index      # node number   (int, node 생성 시 결정)
        self.x = x              # x coordinate  (int, node 생성 시 결정)
        self.y = y              # y coordinate  (int, node 생성 시 결정)
        self.left = left        # left node     (pointer, 자식이 생길 경우 결정)
        self.right = right      # right node    (pointer, 자식이 생길 경우 결정)
        self.parent = parent    # parent node   (pointer, Tree push 시 결정) 

class Tree:
    def __init__(self, root = None):
        self.root = root
        
    def push(self, node):
        if self.root is None:
            self.root = node
            return
        
        value = node.x
        curr, parent = self.root, self.root
        
        while curr is not None:
            parent = curr
            curr = curr.left if value < curr.x else curr.right
            
        node.parent = parent
        if value < parent.x:
            parent.left = node
        else:
            parent.right = node
            
        return
    
    def preorder(self, node, answer):
        if node is not None:
            answer.append(node.index)
            self.preorder(node.left, answer)
            self.preorder(node.right, answer)
            
    def postorder(self, node, answer):
        if node is not None:
            self.postorder(node.left, answer)
            self.postorder(node.right, answer)
            answer.append(node.index)


def solution(nodeinfo):
    answer = [[], []]
    nodeinfo = [[i+1, x, y] for i, (x, y) in enumerate(nodeinfo)] # [number, x, y]
    nodeinfo.sort(key = lambda x: -x[2])
    tree = Tree()
    
    for index, x, y in nodeinfo:
        tree.push(Node(index, x, y))
        
    tree.preorder(tree.root, answer[0])
    tree.postorder(tree.root, answer[1])
    return answer