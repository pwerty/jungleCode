
import sys

def func(arr, target, str, end):
    if(str > end):
        return 0

    if(str == end):
        if(target != arr[str]):
            return 0
        else:
            return 1
        
    mid = (str + end) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return  func(arr, target, str, mid - 1)
    elif arr[mid] < target:
        return func(arr, target, mid + 1, end)
# 찾으면 1, 못찾으면 0을 반환해야하는 문제 상황을 반영했다.

n = int(sys.stdin.readline())
listN = list(map(int, sys.stdin.readline().strip().split()))[:n]

m = int(sys.stdin.readline())
listM = list(map(int, sys.stdin.readline().strip().split()))[:m]


listN.sort()

for i in range (len(listM)):
    print(str(func(listN, listM[i], 0, len(listN) - 1)))