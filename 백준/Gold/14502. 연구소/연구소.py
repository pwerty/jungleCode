from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(field):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if field[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
                field[nx][ny] = 2
                queue.append((nx, ny))
    return sum(row.count(0) for row in field)

empties = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
result = 0
for walls in combinations(empties, 3):
    temp = copy.deepcopy(lab)
    for x, y in walls:
        temp[x][y] = 1
    result = max(result, bfs(temp))
print(result)