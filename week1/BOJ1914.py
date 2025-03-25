import sys
totalValue = 0
result = []

def getMultiple(num):
    return 2 ** num

def goHanoi(diskNum, sr, en):
    global totalValue
    if diskNum == 1: 
        if caseCnt <= 20:  # 최대 20번만 출력
            print('{} {}'. format(sr, en))
        totalValue += 1
        return
    else:
        goHanoi(diskNum - 1, sr, 6 - sr - en)
        if caseCnt <= 20:  # 최대 20번만 출력
            print('{} {}'. format(sr, en))
        totalValue += 1
        goHanoi(diskNum - 1, 6 - sr - en, en)


caseCnt = int(sys.stdin.readline())
hanoiCnt = int(getMultiple(caseCnt)) - 1
print(hanoiCnt)

if(caseCnt <= 20):
    goHanoi(caseCnt, 1, 3)