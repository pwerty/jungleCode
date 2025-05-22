import sys
from collections import deque
input = sys.stdin.readline

garo, sero = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(sero)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS

def BFS():
    while q:
        x, y = q.popleft()
        day = box[x][y] + 1
                # i가 floor, j가 세로, k가 가로이다.
                # 이 상태에서 i[0] == floor | i[1] == sero


        for i in range(4):
            nX = x + dx[i]
            nY = y + dy[i]
            # x, y, z | 행, 열, 높이
            if(nX < 0 or nX >= sero or nY < 0 or nY >= garo):
                continue

            if(box[nX][nY] != 0):
                # 목표는 0이니 0만 찾게 한다.
                continue

            box[nX][nY] = day
            # 값 비교가 필요하겠는데?
            q.append([nX, nY])

            

q = deque()


# BFS

for i in range(sero):
    for j in range(garo):
            if(box[i][j] == 1):
                q.append([i, j])

BFS()

maxValue = 0
isEdible = True
for i in range(sero):
    for j in range(garo):
            if(box[i][j] == 0):
               isEdible = False
                
            maxValue = max(maxValue, int(box[i][j]))


if(isEdible):
    print(str(maxValue - 1))
else:
    print("-1")


