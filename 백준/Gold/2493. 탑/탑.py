import sys

topCnt = int(sys.stdin.readline())
topField = list(map(int, sys.stdin.readline().strip().split()))[:topCnt]
resultArr = [0] * 500001
compareField = []


while len(topField) != 0:
    item = topField.pop()
    itemPos = len(topField) + 1

    canContinue = True
    while canContinue:
        if(len(compareField) == 0):
            itemPair = (item, itemPos)
            compareField.append(itemPair)
            canContinue = False
            continue
        else:
            if(compareField[len(compareField) - 1][0] < item):
                resultApply = compareField.pop()
                resultArr[resultApply[1]] = itemPos
            else:
                itemPair = (item, itemPos)
                compareField.append(itemPair)               
                canContinue = False

for i in range(1, topCnt + 1):
    print(str(resultArr[i]) + " ", end="")
            #compareField.top의 높이..랑 같은 내용