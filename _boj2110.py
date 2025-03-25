import sys

fieldCnt, routerCnt = list(map(int, sys.stdin.readline().strip().split()))
field = []

for i in range(fieldCnt):
     field.append(int(sys.stdin.readline()))

field.sort()

start = 1
end = field[-1] - field[0]

while start <= end:
    mid = (start + end) // 2
    installedCnt = 1
    lastInstalled = field[i]

    for i in range(1, len(field)):
        if field[i] - lastInstalled >= mid:
            installedCnt += 1
            lastInstalled = field[i]


    if installedCnt >= routerCnt:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(f"최적 거리: {result}")
