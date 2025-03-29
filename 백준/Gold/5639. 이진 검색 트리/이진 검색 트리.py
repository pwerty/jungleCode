import sys

sys.setrecursionlimit(2*10**5)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


nodeList = {}

def postOrder(node):
    if(node.left != None):
        postOrder(node.left)

    if(node.right != None):
        postOrder(node.right)

    print(node.value)

def insertNode(value, node):
    if node is None:
        return Node(value)
    else:
        current = node
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
    return node
inputList = []
isFirstInput = True
root = None
while True:
    x= sys.stdin.readline().strip()
    if(isFirstInput):
        isFirstInput = False
        root = insertNode(int(x), None)
        continue
        
        
    if not x:
        break

    x=int(x)
    root = insertNode(x, root)

postOrder(root)