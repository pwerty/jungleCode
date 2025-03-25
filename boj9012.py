import sys

caseCnt = int(sys.stdin.readline())

for i in range(caseCnt):
    sliceTarget = sys.stdin.readline()
    sliced = list(sliceTarget)
    closingCnt = 0
    isVPS = True
    sliced.pop()

    while len(sliced) != 0:
        item = sliced.pop()
        if (item == ")"):
            closingCnt += 1
        else:
            if(closingCnt == 0):
                isVPS = False
                break
            else:
                closingCnt -= 1

    if (closingCnt != 0):
        isVPS = False
        
    if (isVPS):
        print("YES")
    else:
        print("NO")