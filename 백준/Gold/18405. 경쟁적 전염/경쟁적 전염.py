import sys
from collections import deque
input = sys.stdin.readline

mapSize, virusCnt = map(int, input().split())
box = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virusList = []
for i in range(mapSize):
        inputN = list(map(int, input().split()))[:mapSize]
        box.append(inputN)

expectedSec, expectX, expectY = map(int, input().split())

for i in range(mapSize):
    for j in range(mapSize):
        if(box[i][j] != 0):
             virusList.append([box[i][j], i, j, 1])

virusList.sort()
queue = deque()

for i in range(len(virusList)):
     queue.append(virusList[i])

def BFS():
    while queue:
        itemContents, itemX, itemY, itemTime = queue.popleft()

        if(box[expectX - 1][expectY - 1] != 0):
            print(box[expectX - 1][expectY - 1])
            exit()

        if(itemTime > expectedSec + 1):
             print(box[expectX - 1][expectY - 1])
             exit()

        if(box[itemX][itemY] == 0):
            box[itemX][itemY] = itemContents
            
        


        #for i in range(mapSize):
        #    print(box[i])
       # print("-------")
        for i in range(4):
            tX = itemX + dx[i]
            tY = itemY + dy[i]

            if 0 <= tX < mapSize and 0 <= tY < mapSize:
                 if(box[tX][tY] == 0):
                      queue.append([itemContents, tX, tY, itemTime + 1])

BFS()