import sys
treeListCnt, requireTree = list(map(int, sys.stdin.readline().strip().split()))
treeList = list(map(int, sys.stdin.readline().strip().split()))[:treeListCnt]

treeList.sort()
maxTree = treeList[len(treeList) - 1]

def BinarySearch(strt, end):
    mid = (strt + end) // 2

    if(strt > end):
        return -1
    
    if(strt == end):
        return mid
    
    total = 0
    # mid에 대한 값을 treeList 전체에 대조하여 그 결과가 requireTree 와의 차이를 찾아야한다.
    for i in range(len(treeList)):
        addVal = treeList[i] - mid
        if(addVal < 0):
            continue

        total += addVal
        # 15 10 17 20인데 18이 들어오면
        # if(treeList[i]가 mid보다 작으면 패스)
    if total == requireTree:
        return mid
    elif total < requireTree:
        return BinarySearch(strt, mid - 1)
    else:
        return max(mid, BinarySearch(mid + 1, end))
    
print(BinarySearch(0, maxTree))

# 적어도 M미터의 나무를 확보하기
    # 그러면 M자체를 만족하는 시점에서의 최대치를 찾아야겠다.