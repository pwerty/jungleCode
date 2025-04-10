import sys
input = sys.stdin.readline

dp = [float('inf')] * 100001

dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, 100001):
    dp[i] = min(dp[i - 5] + 1, dp[i - 2] + 1)

wanted = int(input())

if(dp[wanted] == float('inf')):
    print('-1')
else:
    print(dp[wanted])