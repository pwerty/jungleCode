import sys

input = sys.stdin.readline

arrASize, arrBSize = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
i = 0
j = 0
totalArr = []

while(i < arrASize and j < arrBSize):
    if(arrA[i] <= arrB[j]):
        totalArr.append(arrA[i])
        i += 1
    elif(arrA[i] > arrB[j]):
        totalArr.append(arrB[j])
        j += 1 

while(i < arrASize):
    totalArr.append(arrA[i])
    i += 1

while(j < arrBSize):
    totalArr.append(arrB[j])
    j += 1

for k in range(len(totalArr)):
    print(f"{totalArr[k]} ", end="")
