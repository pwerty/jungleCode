import sys

numCnt = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))[:numCnt]

operator = list(map(int, sys.stdin.readline().strip().split()))[:4]
maxValue = float('-inf')
minValue = float('inf')

def truncate_division(a, b):
    result = a // b
    if a % b != 0 and ((a < 0) != (b < 0)):  # 음수 방향에서 조정
        result += 1
    return result

def dfs(totalValue, depth):
    global maxValue, minValue
    if(depth == (numCnt)):
        maxValue = max(totalValue, maxValue)
        minValue = min(totalValue, minValue)
    else:
        for i in range(4):
            if(operator[i] > 0):
                operator[i] -= 1
                if i == 0:
                    dfs(totalValue + numList[depth], depth + 1)
                elif i == 1:
                    dfs(totalValue - numList[depth], depth + 1)
                elif i == 2:
                    dfs(totalValue * numList[depth], depth + 1)          
                elif i == 3:
                    dfs(truncate_division(totalValue, numList[depth]), depth + 1)
                operator[i] += 1


dfs(numList[0], 1)
print(maxValue)
print(minValue)
