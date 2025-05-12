import sys
from collections import deque
input = sys.stdin.readline

totalCycle = []

for i in range(4):
    totalCycle.append(list(map(int,input().strip())))

testCaseCnt = int(input())
testCase = deque()
for i in range(testCaseCnt):
    testCase.append(list(map(int, input().split()))[:2])

while(testCase):
    turnCase = deque()
    turnCase.append(testCase.popleft())

    isTurned = [False] * 4
    isScanned = [False] * 4

    while(turnCase):
        whatCycle, turnPos = turnCase.popleft()
        isTurned[whatCycle - 1] = True

        # 회전 대상에 대한 회전 여지 확인
        if whatCycle > 1:  # 첫 번째 톱니바퀴가 아닐 때
            if not (isTurned[whatCycle - 2] or isScanned[whatCycle - 2]):
                if totalCycle[whatCycle - 1][6] != totalCycle[whatCycle - 2][2]:
                    turnCase.append([whatCycle - 1, turnPos * -1])
        
        if whatCycle < 4:  # 마지막 톱니바퀴가 아닐 때
            if not (isTurned[whatCycle] or isScanned[whatCycle]):
                if totalCycle[whatCycle - 1][2] != totalCycle[whatCycle][6]:
                    turnCase.append([whatCycle + 1, turnPos * -1])
        
        # 실제 회전 시작
        # 시계 방향 회전
        if turnPos > 0:
            temp = totalCycle[whatCycle - 1][7]
            for i in range(7, 0, -1):
                totalCycle[whatCycle - 1][i] = totalCycle[whatCycle - 1][i - 1]
            totalCycle[whatCycle - 1][0] = temp
        # 반시계 방향 회전
        else:
            temp = totalCycle[whatCycle - 1][0]
            for i in range(7):
                totalCycle[whatCycle - 1][i] = totalCycle[whatCycle - 1][i + 1]
            totalCycle[whatCycle - 1][7] = temp


                
score = 0
if(totalCycle[0][0] == 1):
    score += 1

if(totalCycle[1][0] == 1):
    score += 2

if(totalCycle[2][0] == 1):
    score += 4

if(totalCycle[3][0] == 1):
    score += 8

print(score)
