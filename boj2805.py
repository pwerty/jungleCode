import sys
sys.setrecursionlimit(10**8)
treeListCnt, requireTree = list(map(int, sys.stdin.readline().strip().split()))
treeList = list(map(int, sys.stdin.readline().strip().split()))[:treeListCnt]
result = []

treeList.sort()
maxTree = treeList[len(treeList) - 1]

def BinarySearch(strt, end):
    global result
    mid = (strt + end) // 2
    if(strt > end):
        return


    total = 0
    # mid에 대한 값을 treeList 전체에 대조하여 그 결과가 requireTree 와의 차이를 찾아야한다.
    for i in range(len(treeList)):
        addVal = treeList[i] - mid
        if(addVal < 0):
            continue

        total += addVal
        # 15 10 17 20인데 18이 들어오면
        # if(treeList[i]가 mid보다 작으면 패스)
    if total >= requireTree:
        result.append(mid)
        return BinarySearch(mid + 1, end)
    elif total < requireTree:
        # 잘린 값이 너무 적으면 자르는 양을 늘려야지 않나?
        return BinarySearch(strt, mid - 1)


BinarySearch(0, maxTree)
print(max(result))
