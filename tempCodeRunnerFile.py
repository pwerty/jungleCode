import sys
totalValue = 0

def getMultiple(num):
    returnValue = 1
    for i in range(num):
        returnValue = returnValue * 2
    return returnValue

def goHanoi(diskNum, sr, en):
    global totalValue
    if diskNum == 1:
        if(caseCnt <= 20):    
            print(f"{sr} {en}")
        totalValue += 1
        return
    else:
        goHanoi(diskNum - 1, sr, 6 - sr - en)
        if(caseCnt <= 20):
            print(f"{sr} {en}")
        totalValue += 1
        goHanoi(diskNum - 1, 6 - sr - en, en)


caseCnt = int(sys.stdin.readline())
hanoiCnt = int(getMultiple(caseCnt)) - 1
print(hanoiCnt)
goHanoi(caseCnt, 1, 3)