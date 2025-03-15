import heapq
import sys

caseCnt = int(sys.stdin.readline())

priority_queue = []
for i in range(caseCnt):
    heapq.heappush(priority_queue, int(sys.stdin.readline()))

while priority_queue:
    print(heapq.heappop(priority_queue))