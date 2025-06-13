import sys
input = sys.stdin.readline

targetLength = int(input())
targetStr = input().strip()
tmpNum = 0
totalNum = 0

for i in range(len(targetStr)):
    if(targetStr[i].isdigit()):
        tmpNum *= 10
        tmpNum += int(targetStr[i])
        if(i == len(targetStr) - 1):
            totalNum += tmpNum
    else:
        totalNum += tmpNum
        tmpNum = 0

print(totalNum)