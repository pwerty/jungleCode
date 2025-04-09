import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())
size = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):  # 구간 길이
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = INF
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + size[i][0] * size[k][1] * size[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n-1])
