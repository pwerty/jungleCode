import sys
input = sys.stdin.readline

numCnt = int(input())
numArr = []
ans = 0

for i in range(0, numCnt):
    numArr.append(int(input()))

for i in range(numCnt - 1, 0, -1):
    if(numArr[i] > numArr[i - 1]):
        continue
    else:
        while (numArr[i] <= numArr[i - 1]):
            numArr[i - 1] -= 1
            ans += 1

print(ans)