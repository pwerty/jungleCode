import sys

nodeCnt = int(sys.stdin.readline())
isVisited = [False] * (nodeCnt + 1)
nodeList = [[] for _ in range(nodeCnt + 1)]
parentsList = [0] * (nodeCnt + 1)

for i in range(nodeCnt - 1):
    inputStr, inputDest = list(map(int, sys.stdin.readline().strip().split()))
    nodeList[inputStr].append(inputDest)
    nodeList[inputDest].append(inputStr)
    # 얘는 필요한가?..
    

def DFS(value):
    dfs_stack = []
    dfs_stack.append(value)

    while len(dfs_stack) != 0:
        item = dfs_stack.pop()

        if(isVisited[item[0]]):
            continue

        isVisited[item[0]] = True
        # 이미 기록되어있으면 스킵하는 경우도 필요할 것 같다.

        if(item[0] == 1):
            pass
        else:
            parentsList[item[0]] = item[1]

        for neighbor in reversed(nodeList[item[0]]):
            if isVisited[neighbor] == False:
                dfs_stack.append((neighbor, item[0]))

DFS([1, 1])

for i in range(len(parentsList)):
    if(parentsList[i] == 0):
        continue
    else:
        print(parentsList[i])