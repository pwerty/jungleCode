import sys
from collections import deque
input = sys.stdin.readline


fieldX, fieldY = list(map(int, input().split()))
isVisited = [[False for _ in range(fieldY)] for _ in range(fieldX)]
campusMap = []
meetCount = 0
q = deque()



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(fieldX):
    campusMap.append(list(input().strip()))

for i in range(fieldX):
    for j in range(fieldY):
        if(campusMap[i][j] == 'I'):
            q.append([i, j])
            isVisited[i][j] = True
            break



while(q):
    x, y = q.popleft()
    if(campusMap[x][y] == 'P'):
        meetCount += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(nx < 0 or nx >= fieldX or ny < 0 or ny >= fieldY):
            continue

        if(campusMap[nx][ny] == 'X'):
            continue

        if(isVisited[nx][ny]):
            continue

        q.append([nx, ny])
        isVisited[nx][ny] = True

if(meetCount == 0):
    print("TT")
else:
    print(meetCount)