# import sys
# input = sys.stdin.readline

# itemCount, backPackStatus = map(int, input().split())
# itemList = []
# maxBagUse = [[0] * (itemCount) for _ in range(backPackStatus + 1)]

# for i in range(itemCount):
#     kg, value = map(int, input().split())
#     itemList.append([kg, value])
#     # 이렇게 되면 itemList[n]의 [0]은 kg, [1]은 value가 된다.


# for i in range(1, backPackStatus + 1):
#     for j in range(itemCount):
#         if(itemList[j][0] > i):
#             maxBagUse[i][j] = maxBagUse[i][j - 1]
#         else:
#             maxBagUse[i][j] = max(maxBagUse[i][j - 1], itemList[j][1] + maxBagUse[i - itemList[j][0]][j - 1])

# print(maxBagUse[backPackStatus][itemCount - 1])

import sys
# import sys
# input = sys.stdin.readline

# itemCount, backPackStatus = map(int, input().split())
# itemList = []
# maxBagUse = [[0] * (itemCount) for _ in range(backPackStatus + 1)]

# for i in range(itemCount):
#     kg, value = map(int, input().split())
#     itemList.append([kg, value])
#     # 이렇게 되면 itemList[n]의 [0]은 kg, [1]은 value가 된다.


# for i in range(1, backPackStatus + 1):
#     for j in range(itemCount):
#         if(itemList[j][0] > i):
#             maxBagUse[i][j] = maxBagUse[i][j - 1]
#         else:
#             maxBagUse[i][j] = max(maxBagUse[i][j - 1], itemList[j][1] + maxBagUse[i - itemList[j][0]][j - 1])

# print(maxBagUse[backPackStatus][itemCount - 1])

import sys
input = sys.stdin.readline

itemCount, backPackStatus = map(int, input().split())
itemList = []
maxBagUse = [[0] * (itemCount + 1) for _ in range(backPackStatus + 1)]  # itemCount + 1로 수정

for i in range(itemCount):
    kg, value = map(int, input().split())
    itemList.append([kg, value])

for i in range(1, backPackStatus + 1):
    for j in range(1, itemCount + 1):  # j를 1부터 시작하도록 수정
        if itemList[j - 1][0] > i:
            maxBagUse[i][j] = maxBagUse[i][j - 1]
        else:
            maxBagUse[i][j] = max(maxBagUse[i][j - 1], itemList[j - 1][1] + maxBagUse[i - itemList[j - 1][0]][j - 1])

print(maxBagUse[backPackStatus][itemCount])