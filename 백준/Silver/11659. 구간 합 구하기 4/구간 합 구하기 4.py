import sys
from collections import deque
input = sys.stdin.readline

numList = [0] * 100001
totalList = [0] * 100001

numCount, testCaseCount = list(map(int, input().split()))

numList = list(map(int, input().split()))

for i in range(0, numCount):
    totalList[i] = totalList[i - 1] + numList[i]

for i in range(testCaseCount):
    start, dest = list(map(int, input().split()))

    if(start == 1):
        print(totalList[dest - 1])
        continue

    if(start == dest):
        print(numList[dest - 1])
        continue

    print(totalList[dest - 1] - totalList[start - 2])
