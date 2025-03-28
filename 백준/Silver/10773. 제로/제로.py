import sys

def empty(idx):
    if myStack[idx] == 0:
        return True
    else:
        return False

def pop(idx):
    if not empty(idx):
        output = myStack[idx]
        myStack[idx] = 0
        return output
    else:
        return -1
    
def push(item, idx):
    myStack[idx] = item
    return 




commandList = int(sys.stdin.readline())
myStack = [0] * 100000
curStackIdx = -1

for i in range(commandList):
    command = int(sys.stdin.readline().strip())

    if command == 0:
        # 여긴 Push N 전용
        popResult = pop(curStackIdx)
        if popResult != -1:
            curStackIdx -= 1
        
    else:
        curStackIdx += 1
        push(command, curStackIdx)
        

total = 0
for i in range(100000):
    total += myStack[i]

print(total)