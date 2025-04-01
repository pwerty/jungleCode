import sys
from collections import deque
input = sys.stdin.readline


cityCnt, roadCnt, dist, start = map(int, input().split())
roadList = [[] for _ in range(cityCnt + 1)]
visited = [-1] * (cityCnt + 1)

for i in range(roadCnt):
    go, arrive = map(int, input().split())
    roadList[go].append(arrive)

def BFS(strValue):
    queue = deque()
    queue.append(strValue)
    while queue:
        item = queue.popleft()


        if(visited[item[0]] != -1):
            continue

        visited[item[0]] = item[1]
        for nextItem in roadList[item[0]]:
            queue.append([nextItem, item[1] + 1])
    
BFS([start, 0])

isHave = False
for i in range(1, cityCnt + 1):
    if(visited[i] == dist):
        print(i)
        isHave = True

if not isHave:
    print("-1")
