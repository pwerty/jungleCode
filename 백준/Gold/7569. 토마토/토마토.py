import sys
from collections import deque
input = sys.stdin.readline

garo, sero, tall = map(int, input().split())
box = [[[0 for col in range(garo)] for row in range(sero)] for depth in range(tall)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(tall):
    for j in range(sero):
        box[i][j] = list(map(int, input().split()))[:garo]
# 가로 세로 층 입력 받고 나면
# [층][행][열] 순으로 접근 한다고 알려져있다.
# box[z][x][y]

# 전체 순회 돌면서 사전에 존재하는 모든 1에 대해 시도
def BFS():

    while q:
        item = q.popleft()
        day = box[item[0]][item[1]][item[2]] + 1
                # i가 floor, j가 세로, k가 가로이다.
                # 이 상태에서 i[0] == floor | i[1] == sero


        for i in range(6):
            nZ = item[0] + dx[i]
            nY = item[1] + dy[i]
            nX = item[2] + dz[i]
            # x, y, z | 행, 열, 높이
            if(nX < 0 or nX >= garo or nY < 0 or nY >= sero or nZ < 0 or nZ >= tall):
                continue

            if(str(box[nZ][nY][nX]) != '0'):
                # 목표는 0이니 0만 찾게 한다.
                continue



            box[nZ][nY][nX] = day
            # 값 비교가 필요하겠는데?

            q.append([nZ, nY, nX])

            

q = deque()

# BFS
for i in range(tall):
    for j in range(sero):
        for k in range(garo):
            if(str(box[i][j][k]) == '1'):
                # 이거 입력 문자열|숫자 여부 잘 봐야함
                q.append([i, j, k])
                # i가 floor, j가 세로, k가 가로이다.
                # 이거 보고나서 BFS 코드 관찰

BFS()
maxValue = 0
isEdible = True
for i in range(tall):
    for j in range(sero):
        for k in range(garo):
            if(str(box[i][j][k]) == '0'):
                isEdible = False
                
            maxValue = max(maxValue, int(box[i][j][k]))


if(isEdible):
    print(str(maxValue - 1))
else:
    print("-1")