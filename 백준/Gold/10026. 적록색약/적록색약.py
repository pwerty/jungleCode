import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

areaSize = int(input())

area = []

duo_q = deque()
tri_q = deque()

duo_cnt = 0
tri_cnt = 0

duo_isVisited = [[False for _ in range(areaSize)] for _ in range(areaSize)]
tri_isVisited = [[False for _ in range(areaSize)] for _ in range(areaSize)]

for i in range(areaSize):
    area.append(list((input().strip())))


for i in range(areaSize):
    for j in range(areaSize):
        if(tri_isVisited[i][j] == False):
            tri_cnt += 1
            tri_q.append([i, j, area[i][j]])

            while(tri_q):
                x, y, color = tri_q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if(0 > nx or nx >= areaSize or 0 > ny or ny >= areaSize):
                        continue

                    if(tri_isVisited[nx][ny] == True):
                        continue

                    if(area[nx][ny] != color):
                        continue

                    tri_isVisited[nx][ny] = True
                    tri_q.append([nx, ny, area[nx][ny]])


        if(duo_isVisited[i][j] == False):
            duo_cnt += 1
            duo_q.append([i, j, area[i][j]])
            
            while(duo_q):
                x, y, color = duo_q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if(0 > nx or nx >= areaSize or 0 > ny or ny >= areaSize):
                        continue

                    if(duo_isVisited[nx][ny] == True):
                        continue

                    if(color == 'R' or color == 'G'):
                        if(area[nx][ny] == 'B'):
                            continue
                    else:
                        if(area[nx][ny] != 'B'):
                            continue

                    duo_isVisited[nx][ny] = True
                    duo_q.append([nx, ny, area[nx][ny]])
                        
print(f"{tri_cnt} {duo_cnt}")