from collections import deque
import sys

# Initialize

arr = [0] * 1001
manCnt, selectNum = list(map(int, sys.stdin.readline().strip().split()))
ansQueue = deque()

for i in range(1, manCnt + 1):
    arr[i] = i


# Counting Session
idx = 1
cnt = 0
while len(ansQueue) != manCnt:
    if arr[idx] != 0:
        cnt += 1
# Moving Session
    
    if cnt == selectNum:
        ansQueue.append(arr[idx])
        arr[idx] = 0
        cnt = 0

    idx = (idx % manCnt) + 1


# Print Session

print("<", end="")
while len(ansQueue) != 0:
    item = ansQueue.popleft()
    if(len(ansQueue) == 0):
        print(str(item) + ">")
    else:
        print(str(item) + ", ", end="")

