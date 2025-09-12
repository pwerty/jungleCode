import sys
input = sys.stdin.readline

bookCnt = int(input())
bookList = list(map(int, input().split()))
ans = 0
isStarting = False
pivotPrice = 0
bookList.sort()
i = 0

while i < bookCnt:
    if(isStarting == False):
        pivotPrice = bookList[i]
        isStarting = True
        

    if(isStarting == True):
        if(bookList[i] >= pivotPrice * 2):
            ans += 1
            isStarting = False
            i -= 1
            
    i += 1


print(ans + 1)
