import heapq, sys

MAXHEAP = []

caseCnt = int(sys.stdin.readline())

for i in range(caseCnt):
    command = int(sys.stdin.readline())

    if command != 0:
         heapq.heappush(MAXHEAP, -command)
    else:
         if(len(MAXHEAP) == 0 ):
            print("0")
         else: 
            print(-heapq.heappop(MAXHEAP))

