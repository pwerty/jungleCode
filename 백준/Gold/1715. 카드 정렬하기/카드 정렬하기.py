import sys, heapq

n = int(sys.stdin.readline())

cards = []
count = 0

for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

while len(cards) != 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    count += temp
    heapq.heappush(cards, temp)

print(count)