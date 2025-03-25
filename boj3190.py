import sys
from collections import deque 

fieldSize = int(sys.stdin.readline())
field = [[0 for j in range(fieldSize + 1 )] for i in range(fieldSize + 1)]
field = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(fieldSize)]                      

itemCnt = int(sys.stdin.readline())
items = []
for i in range(itemCnt):
    itemX, itemY = list(map(int, sys.stdin.readline().strip().split()))
    #pair = (itemX, itemY)
    #items.append(pair)
    field[itemX][itemY] = 9

commandCnt = int(sys.stdin.readline())
commands = deque()
for i in range(commandCnt):
    command = sys.stdin.readline().strip()
    if " " in command:
        # 여긴 Push N 전용
        parts = command.split(" ")
        commandPair = (parts[0], parts[1])
        commands.append(commandPair)


playedSeconds = 0
availablePlay = True
snakeRoute = deque()
gameStart = (1, 1)
snakeRoute.append(gameStart)



while availablePlay: