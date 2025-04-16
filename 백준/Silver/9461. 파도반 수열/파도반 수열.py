import sys
input = sys.stdin.readline
printf = print

testCase = int(input())

dp = [0] * 102

dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3, 101):
    dp[i] = dp[i - 2] + dp[i - 3]


for i in range(testCase):
    target = int(input())
    printf(dp[target - 1])