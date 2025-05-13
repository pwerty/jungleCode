import sys
from collections import deque
input = sys.stdin.readline
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

testCase = int(input())
for i in range(testCase):
    fieldX, fieldY, cabCount = list(map(int, input().split()))
    isVisited = [[False for _ in range(fieldY)] for _ in range(fieldX)]
    field = [[0 for _ in range(fieldY)] for _ in range(fieldX)]
    reqCount = 0
    
    for j in range(cabCount):
        cabX, cabY = list(map(int, input().split()))
        field[cabX][cabY] = 1

    for j in range(fieldX):
        for k in range(fieldY):
            if(isVisited[j][k] == False and field[j][k] == 1):
                q.append([j, k])
                reqCount += 1 

            while(q):
                x, y = q.popleft()
                for l in range(4):
                    nx = x + dx[l]
                    ny = y + dy[l]



                    if(nx < 0 or nx >= fieldX or ny < 0 or ny >= fieldY):
                        continue

                    if(field[nx][ny] == 0):
                        continue

                    if(isVisited[nx][ny] == True):
                        continue

                    

                    isVisited[nx][ny] = True
                    q.append([nx, ny])
    print(reqCount)
    
                    



