import sys

def empty(front, end):
    if end == front:
        return True
    else:
        return False

def size(idx):
    return idx

def pop(fro, en):
    if not empty(fro, en):
        output = myQueue[fro + 1]
        myQueue[fro + 1] = None
        return output
    else:
        return -1
    
def push(item, en):
    myQueue[en] = item
    return 
    # make them front-push

def front(fro, en):
    if not empty(fro, en):
        return myQueue[fro + 1]
    else:
        return -1

def back(fro, en):
    if not empty(fro, en):
        return myQueue[en]
    else:
        return -1

commandList = int(sys.stdin.readline())
myQueue = [None] * 2000000

curFrontIdx = -1
curBackIdx = -1


for i in range(commandList):
    command = sys.stdin.readline().strip()

    if " " in command:
        # 여긴 Push N 전용
        parts = command.split(" ")
        curBackIdx += 1 

        push(parts[1], curBackIdx)
    else:
        if command == "front":
            print(front(curFrontIdx, curBackIdx))
        elif command == "back":
            print(back(curFrontIdx, curBackIdx))
        elif command == "size":
            print(size(curBackIdx - curFrontIdx))
        elif command == "empty":
            if empty(curFrontIdx, curBackIdx) :
                print("1")
            else:
                print("0")
        elif command == "pop":

            popResult = pop(curFrontIdx, curBackIdx)
            if popResult != -1:
                curFrontIdx += 1
            print(popResult)