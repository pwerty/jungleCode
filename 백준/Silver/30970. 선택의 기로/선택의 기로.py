import sys
input = sys.stdin.readline

itemCnt = int(input())
itemList = []
for i in range(itemCnt):
    a, b = map(int, input().split())
    itemList.append([a, b])

sortedForCase1 = sorted(itemList, key=lambda x: (-x[0], x[1]))
sortedForCase2 = sorted(itemList, key=lambda x: (x[1], -x[0]))

print(str(sortedForCase1[0][0]) + " " + str(sortedForCase1[0][1]) + " " + str(sortedForCase1[1][0]) + " " + str(sortedForCase1[1][1]))
print(str(sortedForCase2[0][0]) + " " + str(sortedForCase2[0][1]) + " " + str(sortedForCase2[1][0]) + " " + str(sortedForCase2[1][1]))