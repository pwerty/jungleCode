import sys

shootZoneCnt, animalCnt, shootRange = (map(int, sys.stdin.readline().strip().split()))
shootZoneLst = list(map(int, sys.stdin.readline().strip().split()))
shootZoneLst.sort()
ans = 0

animalLst = [list(map(int, sys.stdin.readline().split())) for _ in range(animalCnt)]

# 정식 식
    # 사대의 위치 x, 동물의 위치 (a, b) 일 때, 이 간의 거리는 | x - a | + b 로 계산한다.
    # 위의 식으로 나온 결과가 사정거리보다 작거나 같아야 한다.
    # 사정거리 >= | 사대 위치 - 동물.X | + 동물.Y
    # 사대 위치가 

    # 안 ㅣ시발 아이디어가 똑같은데, 어떻게 왜 왜 왜왜오애ㅗ애왜왜왜왜

for i, j in animalLst:
    lowVal = i + j - shootRange
    highVal = i - j + shootRange

    left = 0
    right = len(shootZoneLst) - 1

    while left <= right:
        mid = (left + right) // 2
        if(lowVal <= shootZoneLst[mid] <= highVal):
            ans += 1
            break
        elif lowVal > shootZoneLst[mid]:
            left = mid + 1
        elif highVal < shootZoneLst[mid]:
            right = mid - 1
            
print(ans)