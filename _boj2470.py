import sys

caseCnt = int(sys.stdin.readline())
numField = list(map(int, sys.stdin.readline().strip().split()))[:caseCnt]

numField.sort()

startIdx = 0
endIdx = caseCnt - 1
numA = 1000000000
numB = 1000000001

while startIdx != endIdx:
    if(abs(numField[startIdx] + numField[endIdx]) < abs(numA + numB)):
        numA = numField[startIdx]
        numB = numField[endIdx]

    if(numField[startIdx] + numField[endIdx] < 0):
        startIdx += 1
    else:
        endIdx -= 1


print(f"{numA} {numB}")