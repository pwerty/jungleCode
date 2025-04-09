import sys
input = sys.stdin.readline

testCaseCnt = int(input())

for i in range(testCaseCnt):
    applyCnt = int(input())
    result = 1
    originData = []
    for j in range(applyCnt):
        leftRank, rightRank = map(int, input().split())
        originData.append([leftRank, rightRank])

    sortedByL = sorted(originData, key=lambda x: x[0])
    
    LpivotR = sortedByL[0][1]
    for j in range(1, len(originData)):
        if(LpivotR > sortedByL[j][1]):
            result += 1
            LpivotR = sortedByL[j][1]


    print(result)