import sys
input = sys.stdin.readline
dnaCnt, dnaSize = map(int, input().split())
diffCnt = 0
ansDna = ""

dnaList = [list(input().strip()) for _ in range(dnaCnt)]


for i in range(0, dnaSize):
    
    alphabetTable = [0] * 26
    pivotCnt = 0
    selection = 'A'

    for j in range(0, dnaCnt):
        alphabetTable[ord(dnaList[j][i]) - 65] += 1

    for j in range(0, len(alphabetTable)):
        if(alphabetTable[j] > pivotCnt):
            selection = chr(j + 65)
            pivotCnt = alphabetTable[j]

    ansDna += selection
    if(pivotCnt < dnaCnt):
        diffCnt += (dnaCnt - pivotCnt)

print(ansDna)
print(diffCnt)

        

    