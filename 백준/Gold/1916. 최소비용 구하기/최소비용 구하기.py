import heapq
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

vertexCnt = int(input())
edgeCnt = int(input())

adjList = [[] for _ in range(vertexCnt + 1)]
INF = float('inf')
dist = [INF] * (vertexCnt + 1)

for _ in range(edgeCnt):
    start, dest, cost = map(int, input().split())
    adjList[start].append((cost, dest))

startNode, destNode = map(int, input().split())

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        curCost, curNode = heapq.heappop(pq)

        if dist[curNode] < curCost:
            continue

        for nextCost, nextNode in adjList[curNode]:
            newCost = curCost + nextCost
            if newCost < dist[nextNode]:
                dist[nextNode] = newCost
                heapq.heappush(pq, (newCost, nextNode))

dijkstra(startNode)


print(dist[destNode])
