import sys
import array

# counting sort
arr = array.array('i', [0] * 10001)
caseCnt = int(sys.stdin.readline().strip())

for i in range(caseCnt):
    inputNum = int(sys.stdin.readline().strip())
    arr[inputNum] += 1

for i in range(len(arr)):
    while arr[i] != 0:
        arr[i] -= 1
        print(str(i)) 