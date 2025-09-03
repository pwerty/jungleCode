import sys
input = sys.stdin.readline
from bisect import bisect_right
from itertools import accumulate

studentCnt, candyCnt = map(int, input().split())
scoreList = list(map(int, input().split()))
scoreList.sort()


cutLineStart = 0
cutLineEnd = scoreList[-1]
successCount = cutLineEnd

prefix = [0] + list(accumulate(scoreList)) 

while cutLineStart <= cutLineEnd:
    cutLine = (cutLineStart + cutLineEnd) // 2
    
    idx = bisect_right(scoreList, cutLine)
    total = prefix[-1] - prefix[idx]
    count = len(scoreList) - idx
    tmpCandyCnt = total - cutLine * count

    if tmpCandyCnt <= candyCnt:
        successCount = cutLine
        cutLineEnd = cutLine - 1
    else:
        cutLineStart = cutLine + 1


print(successCount)
