import sys
from collections import deque
input = sys.stdin.readline

roomStatus = []
roomSize = int(input().strip())
visitCnt = [[float('inf') for _ in range(roomSize)] for _ in range(roomSize)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(roomSize):
    line = input().strip()
    roomStatus.append([int(room) for room in line])

queue = deque()
queue.append([0, 0, 0])

while queue:
    item = queue.popleft()

    for i in range(4):
        tmpX = item[0] + dx[i]
        tmpY = item[1] + dy[i]
        tmpVC = item[2]
        isWall = False

        if(tmpX < 0 or tmpX >= roomSize or tmpY < 0 or tmpY >= roomSize):
            continue

        new_broken_walls = tmpVC + (1 if roomStatus[tmpX][tmpY] == 0 else 0)

        if new_broken_walls < visitCnt[tmpX][tmpY]:
                visitCnt[tmpX][tmpY] = new_broken_walls
                queue.append((tmpX, tmpY, new_broken_walls))    

print(visitCnt[roomSize - 1][roomSize - 1])