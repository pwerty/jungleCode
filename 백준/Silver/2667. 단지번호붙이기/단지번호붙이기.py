import sys
from collections import deque
input = sys.stdin.readline

fieldLength = int(input())

isVisited = [[False] * fieldLength for _ in range(fieldLength)]
fieldStatus = []

for _ in range(fieldLength):
    fieldStatus.append(input().rstrip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ansArr = []

def BFS(strItem):
    global areaCnt
    queue = deque()
    queue.append(strItem)

    thisFieldSize = 0
    while queue:
        x, y = queue.popleft()
        
        if(isVisited[x][y]):
            continue

        thisFieldSize += 1
        isVisited[x][y] = True

        for i in range(4):
            tX = x + dx[i]
            tY = y + dy[i]

            if 0 <= tX < fieldLength and 0 <= tY < fieldLength:
                if(fieldStatus[tX][tY] == "1" and isVisited[tX][tY] == False):
                    queue.append([tX, tY])
    return thisFieldSize


areaCnt = 0
for i in range(fieldLength):
    for j in range(fieldLength):
        if(fieldStatus[i][j] == "1" and isVisited[i][j] == False):
            ansArr.append(BFS([i, j]))
            areaCnt += 1
            

ansArr.sort()

print(areaCnt)
for i in range(len(ansArr)):
    print(ansArr[i])
