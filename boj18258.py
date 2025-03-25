import sys



def empty(idx):
    if myQueue[idx] is None:
        return True
    else:
        return False

def size(idx):
    return idx

def pop(idx):
    if not empty(idx):
        output = myQueue[idx]
        myQueue[idx] = None
        return output
    else:
        return -1
    
def push(item, idx):
    myQueue[idx] = item
    return 
    # make them front-push

def front(idx):
    if not empty(idx):
        return myQueue[idx]
    else:
        return -1

def back(idx):
    if not empty(idx):
        return myQueue[idx]
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
            print(front(curFrontIdx + 1))
        elif command == "back":
            print(back(curBackIdx))
        elif command == "size":
            print(size(curBackIdx - curFrontIdx))
        elif command == "empty":
            if empty(curBackIdx) :
                print("1")
            else:
                print("0")
        elif command == "pop":

            popResult = pop(curFrontIdx + 1)
            if popResult != -1:
                curFrontIdx += 1
            print(popResult)