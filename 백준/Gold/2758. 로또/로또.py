import sys
input = sys.stdin.readline

caseCnt = int(input())
for a in range(caseCnt):
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(1, m + 1):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(1, m + 1):
            if j % 2 != 0:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j//2]

    result = sum(dp[n])
    print(result)