import sys

def empty(idx):
    if myStack[idx] is None:
        return True
    else:
        return False

def top(idx):
    if not empty(idx):
        return myStack[idx]
    else:
        return -1

def size(idx):
    return idx + 1

def pop(idx):
    if not empty(idx):
        output = myStack[idx]
        myStack[idx] = None
        return output
    else:
        return -1
    
def push(item, idx):
    myStack[idx] = item
    return 




commandList = int(sys.stdin.readline())
myStack = [None] * 10000
curStackIdx = -1

for i in range(commandList):
    command = sys.stdin.readline().strip()

    if " " in command:
        # 여긴 Push N 전용
        parts = command.split(" ")
        curStackIdx += 1 

        push(parts[1], curStackIdx)
    else:
        if command == "top":
            print(top(curStackIdx))
           
        elif command == "size":

            print(size(curStackIdx))
        elif command == "empty":

            if empty(curStackIdx) :
                print("1")
            else:
                print("0")
        elif command == "pop":

            popResult = pop(curStackIdx)
            if popResult != -1:
                curStackIdx -= 1
            print(popResult)