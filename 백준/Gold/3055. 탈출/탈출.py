import sys
from collections import deque

input = sys.stdin.readline

fieldX, fieldY = map(int, input().split())
fieldStatus = [list(input().strip()) for _ in range(fieldX)]

waterStatus = [[-1] * fieldY for _ in range(fieldX)]
playerStatus = [[-1] * fieldY for _ in range(fieldX)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 초기화
waterQ = deque()
playerQ = deque()

for i in range(fieldX):
    for j in range(fieldY):
        if fieldStatus[i][j] == '*':  # 물 시작점
            waterStatus[i][j] = 0
            waterQ.append((i, j))
        elif fieldStatus[i][j] == 'S':  # 플레이어 시작점
            playerStatus[i][j] = 0
            playerQ.append((i, j))
        elif fieldStatus[i][j] == 'X':  # 돌
            waterStatus[i][j] = float('inf')
            playerStatus[i][j] = float('inf')

# 물 확산 처리
while waterQ:
    x, y = waterQ.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < fieldX and 0 <= ny < fieldY:
            if waterStatus[nx][ny] == -1 and fieldStatus[nx][ny] not in ('X', 'D'):
                waterStatus[nx][ny] = waterStatus[x][y] + 1
                waterQ.append((nx, ny))

# 플레이어 이동 처리
while playerQ:
    x, y = playerQ.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < fieldX and 0 <= ny < fieldY:
            # 목표 지점에 도달한 경우
            if fieldStatus[nx][ny] == 'D':
                print(playerStatus[x][y] + 1)
                exit()
            # 물보다 먼저 이동할 수 있는 경우
            if playerStatus[nx][ny] == -1 and (waterStatus[nx][ny] == -1 or playerStatus[x][y] + 1 < waterStatus[nx][ny]):
                playerStatus[nx][ny] = playerStatus[x][y] + 1
                playerQ.append((nx, ny))

print("KAKTUS")
