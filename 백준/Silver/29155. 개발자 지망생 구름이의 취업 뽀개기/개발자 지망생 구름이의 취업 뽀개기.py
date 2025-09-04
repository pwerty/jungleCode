import sys
input = sys.stdin.readline

caseCnt = int(input())
taskList = list(map(int, input().split()))

caseList = []

for i in range(caseCnt):
    a, b = map(int, input().split())
    caseList.append([a, b])

sortedCaseList = sorted(caseList, key=lambda x: (x[0], x[1]))
caseIdx = 0
taskIdx = 0
timeTotal = 0

while(len(taskList) != taskIdx):
    beforeSession = [0, 0]
    if(taskList[taskIdx] != 0 and taskIdx != 0):
        timeTotal += 60

    while(taskList[taskIdx] != 0):
        if(sortedCaseList[caseIdx][0] == taskIdx + 1):
            timeTotal += sortedCaseList[caseIdx][1]


            if(beforeSession[0] != 0):
                if(beforeSession[0] == sortedCaseList[caseIdx][0]):
                    timeTotal += abs(beforeSession[1] - sortedCaseList[caseIdx][1])

            beforeSession = sortedCaseList[caseIdx]
            taskList[taskIdx] -= 1
            caseIdx += 1
        else:
            caseIdx += 1
    taskIdx += 1
    
        


print(timeTotal)