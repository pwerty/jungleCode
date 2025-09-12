from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
fullMap = [list(map(int,input().strip())) for _ in range(h)]
offset = [(1, 0), (-1, 0), (0, 1), (0, -1)]
isMap = lambda x,y : 0<= x < w and 0 <= y < h

def bfs(x, y, range):
    isVisited[y][x] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in offset:
            nx, ny = x + dx, y + dy
            if(isMap(nx, ny) and not isVisited[ny][nx] and fullMap[ny][nx]):
                isVisited[ny][nx] = True
                q.append((nx, ny))


def spread():
    nextMap = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            spreadRange = fullMap[i][j]
            nextMap[i][j] = max(nextMap[i][j], fullMap[i][j])

            if(spreadRange):
                for nextX in range(j - spreadRange, j + spreadRange + 1 ):
                    for nextY in range(i - spreadRange, i + spreadRange + 1 ):
                        if(isMap(nextX,nextY) and fullMap[nextY][nextX] < fullMap[i][j]):
                            nextMap[nextY][nextX] = max(nextMap[nextY][nextX], fullMap[i][j])
    return nextMap

def check():
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if(fullMap[i][j] and not isVisited[i][j]):
                bfs(j, i, fullMap[i][j])
                cnt += 1
    return cnt

day = 0
isVisited = [[False for _ in range(w)] for _ in range(h)]
chunkCnt = check()

while(chunkCnt > 1):
    isVisited = [[False for _ in range(w)] for _ in range(h)]
    day += 1
    fullMap = spread()
    chunkCnt = check()
print(day)

    
