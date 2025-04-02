import sys, heapq
input = sys.stdin.readline

nodeCnt = int(input())

graph = [[] for _ in range(nodeCnt + 1)]
tmp = []

for _ in range(nodeCnt):
    tmp.append(input().rstrip())

outdegree = [0] * (nodeCnt + 1)
change = [0] * (nodeCnt + 1)

heap = []

for i in range(nodeCnt):
    for j in range(nodeCnt):
        if tmp[i][j] == '1':
            graph[j + 1].append(i + 1)
            outdegree[i + 1] += 1
    if outdegree[i + 1] == 0:
        heapq.heappush(heap, -(i + 1))

num = nodeCnt
while heap:
    now = -heapq.heappop(heap)
    change[now] = num
    num -= 1

    for next_node in graph[now]:
        outdegree[next_node] -= 1
        if outdegree[next_node] == 0:
            heapq.heappush(heap, -next_node)

print(*change[1:]) if not 0 in change[1:] else print(-1)

        