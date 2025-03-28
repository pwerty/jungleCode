numList = [int(input()) for i in range(0, 9)]
maxItem = 0

for i in range(0, 9):
    maxItem = max(maxItem, numList[i])

for i in range(0, 9):
    if numList[i] == maxItem:
        print(str(numList[i]))
        print(str(i + 1))