import sys
input = sys.stdin.readline
bucketList = []
cageMap = [0] * 1000001
bucketCnt, moveDistance = map(int, input().split())

for i in range(bucketCnt):
    a, b = map(int, input().split())
    cageMap[b] = a

posStart = moveDistance
value = sum(cageMap[0:(2 * moveDistance + 1)])
maxValue = value

for i in range(posStart + 1, len(cageMap) - 1 - moveDistance):
    value = (value - cageMap[i - moveDistance - 1] + cageMap[i + moveDistance])
    maxValue = max(maxValue, value)


print(maxValue)
