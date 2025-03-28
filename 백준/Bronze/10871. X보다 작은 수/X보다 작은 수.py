inputNumCnt, inputTargetNum = input().split()
inputNumCnt = int(inputNumCnt)
inputTargetNum = int(inputTargetNum)
numList = list(map(int, input().strip().split()))[:inputNumCnt]

for i in range(0, inputNumCnt):
    if numList[i] < inputTargetNum:
        print(str(numList[i]) + " ", end="")