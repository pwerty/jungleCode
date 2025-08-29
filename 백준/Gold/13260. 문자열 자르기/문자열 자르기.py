import sys
input = sys.stdin.readline

# 무식하게 큰것부터 자르면 되지 않을까?
    # 반박 ..!!
    # 20 2
    # 무식한 방법 : 15 10 : cost20, cost15 = 35
    # 더 적은 답 : 10 15 : cost20, cost10 = 30
    # 정렬하고 무식자르기는 불가능

stringLength, commandCnt = map(int, input().split())
commandList = []
commandList = list(map(int, input().split()))

p = [0] + commandList + [stringLength]
p.sort()


dp = [[0] * (commandCnt + 2) for _ in range(commandCnt + 2)]
# Knuth-Yao Moment #1
opt = [[0] * (commandCnt + 2) for _ in range(commandCnt + 2)]

for i in range(commandCnt + 1):
    opt[i][i+1] = i + 1
for length in range(2, commandCnt + 2):
    for i in range(commandCnt + 2 - length):
        j = i + length
        
        min_val = float('inf')
        
        # Knuth-Yao Moment #2
        start_k = opt[i][j-1]
        end_k = opt[i+1][j]
        
        for k in range(start_k, end_k + 1):
            current_k_cost = dp[i][k] + dp[k][j]
            if current_k_cost < min_val:
                min_val = current_k_cost
                opt[i][j] = k
        
        if min_val != float('inf'):
            dp[i][j] = (p[j] - p[i]) + min_val

print(dp[0][commandCnt + 1])