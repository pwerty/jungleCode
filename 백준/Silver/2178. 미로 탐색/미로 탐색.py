import sys
from collections import deque

destX, destY = list(map(int, sys.stdin.readline().strip().split()))
maze = []
visitedCnt = [[-1]*destY for _ in range(destX)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]



for i in range(destX):
    mazeLine = sys.stdin.readline().strip()
    maze.append(mazeLine)

def bfs():
    standardQueue = deque()
    standardQueue.append([0, 0, 1])
    visitedCnt[0][0] = 1
    
    while standardQueue:
        item = standardQueue.popleft()

        for i in range(4):
            tmpX = item[0] + dx[i]
            tmpY = item[1] + dy[i]
            stepCnt = item[2] + 1

            if(tmpX < 0 or tmpX >= destX or tmpY < 0 or tmpY >= destY):
                continue

            if(visitedCnt[tmpX][tmpY] != -1):
                continue

            if(maze[tmpX][tmpY] == '0'):
                continue



            visitedCnt[tmpX][tmpY] = stepCnt
            standardQueue.append([tmpX, tmpY, stepCnt])




bfs()
print(visitedCnt[destX - 1][destY - 1])