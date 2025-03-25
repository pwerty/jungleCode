from collections import deque
import sys

theQueue = deque()

numberSelection = int(sys.stdin.readline())

for i in range(numberSelection , 0, -1):
    theQueue.append(i)

while len(theQueue) != 1:
    theQueue.pop()
    if(len(theQueue) == 1):
        continue
    toFront = theQueue.pop()
    theQueue.appendleft(toFront)

print(theQueue[0])