paperX, paperY = input().split()
paperX = int(paperX)
paperY = int(paperY)
areaList = []
areaList.append([0, paperY, 0, paperX])
# 한 뭉치에서 각각 strX, endX, strY, endY를 정의합니다

cutActionCnt = int(input())

for i in range(cutActionCnt):
    commandCode, cutAxis = input().split()
    commandCode = int(commandCode)
    cutAxis = int(cutAxis)

    if commandCode == 0: # 가로 커팅
        for j in range(len(areaList)):
            # areaList 내의 아이템 중 커팅으로 인한 영향권에 들어오는 범위를 조사해야합니다.
            # 그럼 이미 존재하는 범위 사이에 있어야하니 str와 end 사이에 있으면 영향권이라고 할 수 있겠네요?
            if cutAxis > areaList[j][0] and cutAxis < areaList[j][1]:
                # 여긴 해당되는 영역을 다시 split 하는 코드입니다.
                # 우선 remove를 하면 배열이 변해버리니 나중에 비활성화 하기 위해 값을 임시 저장하고 배열 값은 0으로 만듭시다.
                strX = areaList[j][0]
                endX = areaList[j][1]

                strY = areaList[j][2]
                endY = areaList[j][3]

                areaList.append([strX, cutAxis, strY, endY])
                areaList.append([cutAxis, endX, strY, endY])

                for k in range(0, 4):
                    areaList[j][k] = 0
    else: # 세로 커팅
        for j in range(len(areaList)):
            # areaList 내의 아이템 중 커팅으로 인한 영향권에 들어오는 범위를 조사해야합니다.
            # 그럼 이미 존재하는 범위 사이에 있어야하니 str와 end 사이에 있으면 영향권이라고 할 수 있겠네요?
            if cutAxis > areaList[j][2] and cutAxis < areaList[j][3]:
                # 여긴 해당되는 영역을 다시 split 하는 코드입니다.
                # 우선 remove를 하면 배열이 변해버리니 나중에 비활성화 하기 위해 값을 임시 저장하고 배열 값은 0으로 만듭시다.
                strX = areaList[j][0]
                endX = areaList[j][1]

                strY = areaList[j][2]
                endY = areaList[j][3]

                areaList.append([strX, endX, strY, cutAxis])
                areaList.append([strX, endX, cutAxis, endY])

                for k in range(0, 4):
                    areaList[j][k] = 0

# 모든 커팅이 끝났습니다.

a = 0
while a < len(areaList):
    if areaList[a][1] == 0 and areaList[a][3] == 0:
        del areaList[a]
    else:
        a += 1

maxSize = 0

for i in range(len(areaList)):

    needCompare = ((areaList[i][1] - areaList[i][0]) * (areaList[i][3] - areaList[i][2]))
    maxSize = max(maxSize, needCompare)

print(maxSize)