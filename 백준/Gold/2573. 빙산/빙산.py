import sys
input = sys.stdin.readline
from collections import deque

sero, garo = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(sero)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

day = 0
expectedValue = 0

def dfs(x, y):
    stack = [(x, y)]
    isVisited[x][y] = True
    visitedCount = 1
    meltingQueue = deque()

    while stack:
        cx, cy = stack.pop()
        meltValue = 0

        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]

            if 0 <= nx < sero and 0 <= ny < garo:
                if field[nx][ny] == 0:
                    meltValue += 1
                elif not isVisited[nx][ny]:
                    isVisited[nx][ny] = True
                    visitedCount += 1
                    stack.append((nx, ny))

        meltingQueue.append((cx, cy, meltValue))

    meltedZoneCnt = 0
    while meltingQueue:
        mx, my, melt = meltingQueue.popleft()
        if field[mx][my] - melt <= 0:
            field[mx][my] = 0
            meltedZoneCnt += 1
        else:
            field[mx][my] -= melt

    return visitedCount, meltedZoneCnt


while True:
    isVisited = [[False] * garo for _ in range(sero)]
    isFounded = False  # 빙산 찾았는지 여부

    for i in range(sero):
        for j in range(garo):
            if field[i][j] != 0 and not isVisited[i][j]:
                isFounded = True
                visitedCount, meltedZoneCnt = dfs(i, j)

                if expectedValue != 0 and expectedValue != visitedCount:
                    print(day)
                    sys.exit()

                expectedValue = visitedCount - meltedZoneCnt
                if expectedValue == 0:  # 전부 녹음
                    print(0)
                    sys.exit()

                day += 1

    if not isFounded:  # 빙산 자체가 없음
        print(0)
        sys.exit()
