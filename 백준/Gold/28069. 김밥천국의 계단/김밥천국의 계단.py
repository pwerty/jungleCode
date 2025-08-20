import sys
input = sys.stdin.readline

goal, step = map(int, input().split())
dp = [1000000000 for _ in range(goal+1)]
dp[0] = 0
# 3.
for i in range(1,  goal+1) :
    # 3-1. 이전 계단에서 올라오는 경우
    dp[i] = min(dp[i], dp[i-1] + 1)
    # 3-2. 순간이동이 가능한 경우
    if i + i // 2 <= goal :
        dp[i + i // 2] = min(dp[i + i // 2], dp[i] + 1)
# 4. 결과 출력
print("minigimbob" if dp[-1] <= step else "water")