import sys
input = sys.stdin.readline

curHealth, requested = map(int, input().split())
requestedList = list(map(int, input().split()))
isContinue = True
ans = 0

requestedList.sort()
if(curHealth >= 200):
    isContinue = False

if(isContinue):
    for i in range(requested):
        curHealth += requestedList[i]
        ans += 1
        if(curHealth >= 200):
            break

print(ans)