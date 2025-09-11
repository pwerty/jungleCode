# from collections import deque

# input = sys.stdin.readline

# def isInRange(num):
#     if num >= 129 and num <= 138:
#         return True
#     else:
#         return False

# ans = 0
# drinkCnt, drinkTry = map(int, input().split())

# drinkList = list(map(int, input().split()))
# q = deque(drinkList)
# for i in range(drinkTry):
#     q.appendleft(0)
#     q.append(0)
# print(drinkList)
# drinkTotal = sum(drinkList[0:drinkTry])

# if(isInRange(drinkTotal)):
    
#     isProgrammable = True
#     ans += 1

# for i in range(1, len(drinkList) - drinkTry + 1):
#     drinkTotal -= drinkList[i - 1]
#     drinkTotal += drinkList[i - 1 + drinkTry]

#     if(isInRange(drinkTotal)):
#         ans += 1

# print(ans)
import sys
input = sys.stdin.readline

drinkCnt, drinkTry = map(int, input().split())
drink = list(map(int,input().split()))

cnt = 0
prefix = [0]
for i in range(1,drinkCnt+1):
    prefix.append(prefix[i-1]+drink[i-1])
    if i > drinkTry:
        prefix[i] -= drink[i-drinkTry-1]
    if prefix[i] >= 129 and prefix[i] <= 138:
        cnt += 1

print(cnt)