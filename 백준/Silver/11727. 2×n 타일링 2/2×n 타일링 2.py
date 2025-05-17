import sys
from collections import deque
input = sys.stdin.readline

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4, 1001):
    dp[i] = dp[i - 1] +  (dp[i - 2] * 2)

num = int(input())
print(dp[num] % 10007)

