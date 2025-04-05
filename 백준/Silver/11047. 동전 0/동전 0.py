import sys
input = sys.stdin.readline

coinCnt, req = map(int, input().split())
coinList = [0] * coinCnt
resultCnt = 0

for i in range(coinCnt):
    insertCoin = int(input())
    coinList[i] = insertCoin

coinList.sort(reverse=True)

for coin in coinList:
    while req >= coin:
        resultCnt += req // coin
        req %= coin
        


print(resultCnt)