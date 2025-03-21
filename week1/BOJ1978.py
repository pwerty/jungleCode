def isPrimeNum(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True
        
listCnt = int(input())
numList = list(map(int, input().strip().split()))[:listCnt + 1]

ans = 0

for i in range(len(numList)):
    if isPrimeNum(numList[i]):
        ans += 1

print(str(ans))