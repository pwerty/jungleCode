import sys
from collections import deque

nodeCnt = int(sys.stdin.readline())
edgeCnt = int(sys.stdin.readline())
startNde = 1
nodeList = [[] for _ in range(nodeCnt + 1)]
isVisited = [False] * (nodeCnt + 1)
detectedCnt = 0

for i in range(edgeCnt):
    edgeStart, edgeEnd = map(int, sys.stdin.readline().split())
    nodeList[edgeStart].append(edgeEnd)
    
    # 얘는 필요한가?..
    nodeList[edgeEnd].append(edgeStart)
    # 이러면 모든 정점은 nodeList에 입력이 완료 된다.

# 전제 조건을 만족한다 : 방문 할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문 한다.
for edges in nodeList:
    edges.sort()

visitStack = []
visitQueue = deque()

def dfs(strNode):
    # Completed
    global detectedCnt
    visitStack = []
    visitStack.append(strNode)

    while len(visitStack) != 0:
        # while visitStack not empty
        item = visitStack.pop()
    
        if(isVisited[item]):
            continue
    
        isVisited[item] = True
        detectedCnt += 1

        for sideItem in sorted(nodeList[item], reverse=True):
            if not isVisited[sideItem]:
                visitStack.append(sideItem)

dfs(startNde)
print(detectedCnt - 1)