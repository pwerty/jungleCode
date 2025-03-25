import sys

# 11053 여기에 잠들다 11시 34분
# 최선을 다해서 풀었지만 시간초과로 더 이상 수행 할 수가 없다.
fieldLength = int(sys.stdin.readline())
field = list(map(int, sys.stdin.readline().strip().split()))[:fieldLength]
memo = {}

def getMore(reqCount, lastIdx, selectedCnt):

    if(reqCount, lastIdx, selectedCnt) in memo:
        return memo[(reqCount, lastIdx, selectedCnt)]

    if reqCount == selectedCnt:
        return True
    
    for i in range(lastIdx + 1, fieldLength):
        if(field[i] > field[lastIdx]):
            if(reqCount - selectedCnt <= fieldLength - i):
                canContinue = getMore(reqCount, i, selectedCnt + 1)
                if canContinue: 
                    memo[(reqCount, lastIdx, selectedCnt)] = True
                    return True
            else:
                memo[(reqCount, lastIdx, selectedCnt)] = False
                return False

                
    memo[(reqCount, lastIdx, selectedCnt)] = False
    return False


def binarySearch(start, end):
    result = 0
    
    while start <= end:
        canNext = False

        mid = (start + end) // 2
        for i in range(fieldLength):
           if mid > fieldLength - i:
                break
           
           canNext = getMore(mid, i, 1)
           if(canNext):
                break
              
        if(canNext):
            result = max(result, mid)
            start = mid + 1
        else:
            end = mid - 1
        
    if(start > end):
            if(result == 0):
                return 1
            return result
    
print(binarySearch(0, fieldLength))