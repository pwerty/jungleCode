import sys

stickStack = []

stickCnt = int(sys.stdin.readline())

for i in range(stickCnt):
    stickStack.append(int(sys.stdin.readline()))

curMaxLength = 0
viewAbleCnt = 0

while len(stickStack) != 0:
    item = stickStack.pop()

    if(curMaxLength < item):
        curMaxLength = item
        viewAbleCnt += 1

print(viewAbleCnt)   