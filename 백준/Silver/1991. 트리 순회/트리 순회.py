import sys

nodeCnt = int(sys.stdin.readline())
nodes = []
for i in range(nodeCnt):
    command = sys.stdin.readline().strip()
    parts = command.split(" ")

    nodes.append([parts[0], parts[1], parts[2]])


def preorder(node):
    print(node.data, end="")

    if(node.left != None):
        preorder(node.left)

    if(node.right != None):
        preorder(node.right)

def inorder(node):
    if(node.left != None):
        inorder(node.left)

    print(node.data, end="")


    if(node.right != None):
        inorder(node.right)

def postorder(node):
    if(node.left != None):
        postorder(node.left)
    if(node.right != None):
        postorder(node.right)

    print(node.data, end="")



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 트리 생성 함수
def create_tree(nodes):
    node_map = {}  # 노드 참조를 저장할 맵
    for curNode, leftNode, rightNode in nodes:
        if curNode not in node_map:
            node_map[curNode] = Node(curNode)  # 현재 노드 생성
        if leftNode != ".":  
            if leftNode not in node_map:
                node_map[leftNode] = Node(leftNode)  # 좌측 자식 노드 생성
            node_map[curNode].left = node_map[leftNode]  # 연결 설정
        if rightNode != ".":  # 우측 자식이 있는 경우
            if rightNode not in node_map:
                node_map[rightNode] = Node(rightNode)  # 우측 자식 노드 생성
            node_map[curNode].right = node_map[rightNode]  # 연결 설정
    return node_map[nodes[0][0]]  # 루트 노드 반환

# 트리 생성
root = create_tree(nodes)

preorder(root)
print("")
inorder(root)
print("")
postorder(root)
