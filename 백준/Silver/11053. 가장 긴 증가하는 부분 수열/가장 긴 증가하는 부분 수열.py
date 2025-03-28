import sys, bisect

fieldLength = int(sys.stdin.readline())
field = list(map(int, sys.stdin.readline().strip().split()))[:fieldLength]

def longestIncreasingSubsequence(arr, arrLength):
    tmp = []
    tmp.append(arr[0])
    theLength = 1
    for i in range(1, arrLength):
        if(arr[i] > tmp[theLength - 1]):
            tmp.append(arr[i])
            theLength += 1

        else:
            ind = bisect.bisect_left(tmp, arr[i])
            tmp[ind] = arr[i]
    return theLength


print(longestIncreasingSubsequence(field, fieldLength))