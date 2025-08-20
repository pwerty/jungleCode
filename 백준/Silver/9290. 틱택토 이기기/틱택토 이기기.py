import sys
input = sys.stdin.readline

stageNum = int(input())
boardList = []

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [1, -1, 1, -1, 0, 1, -1, 0]

for i in range(stageNum):
    board = [list(input().strip()) for _ in range(3)]
    winPlayer = input().strip()
    boardList.append(board)

    placed = False 

    for j in range(9):
        if placed:
            break
        x, y = j // 3, j % 3
        if board[x][y] != winPlayer:
            continue

        for k in range(8):
            tmpX = x + dx[k]
            tmpY = y + dy[k]

            if not (0 <= tmpX < 3 and 0 <= tmpY < 3):
                continue

            vecX = dx[k]
            vecY = dy[k]

            nxtX = tmpX + vecX
            nxtY = tmpY + vecY

            if not (0 <= nxtX < 3 and 0 <= nxtY < 3):
                continue

            # 패턴 1: winPlayer - empty - winPlayer
            if board[tmpX][tmpY] == '-' and board[nxtX][nxtY] == winPlayer:
                board[tmpX][tmpY] = winPlayer
                placed = True
                break

            # 패턴 2: winPlayer - winPlayer - empty
            if board[tmpX][tmpY] == winPlayer and board[nxtX][nxtY] == '-':
                board[nxtX][nxtY] = winPlayer
                placed = True
                break

# 출력
for idx, board in enumerate(boardList, 1):
    print(f"Case {idx}:")
    for row in board:
        print("".join(row))
