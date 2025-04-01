from collections import deque
import sys
input = sys.stdin.readline

stdCnt, compareNum = map(int, input().split())
compareList = [[] for _ in range(stdCnt + 1)]
degreeList = [0] * (stdCnt + 1)

for i in range(compareNum):
    compA, compB = map(int, input().split())
    compareList[compA].append(compB)
    degreeList[compB] += 1

queue = deque()
for i in range(1, stdCnt + 1):
    if(degreeList[i] == 0):
        queue.append(i)

while queue:
    cur = queue.popleft()
    print(str(cur) + " ", end="")

    for nextItem in compareList[cur]:
        degreeList[nextItem] -= 1
        if(degreeList[nextItem] == 0):
            queue.append(nextItem)