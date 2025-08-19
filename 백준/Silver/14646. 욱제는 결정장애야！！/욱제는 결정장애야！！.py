import sys
input = sys.stdin.readline


n = int(input())
arr = [0] * (n + 1)
selection = list(map(int,input().split()))

maxSticker = 0
stickerCount = 0


for i in range(0, len(selection)):
    if(arr[selection[i]] == 0):
        arr[selection[i]] = 1
        stickerCount += 1
    else:
        arr[selection[i]] = 0
        stickerCount -= 1
    
    maxSticker = max(maxSticker, stickerCount)

print(maxSticker)