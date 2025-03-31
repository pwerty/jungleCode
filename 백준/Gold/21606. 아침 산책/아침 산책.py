import sys
sys.setrecursionlimit(10**6)
caseCnt = int(sys.stdin.readline())
areaStatus = sys.stdin.readline()
edgeList = [[] for _ in range(caseCnt + 1)]
goAvailable = 0

for i in range(caseCnt - 1):
    
    start, dest = list(map(int, sys.stdin.readline().strip().split()))
    edgeList[start].append(dest)
    edgeList[dest].append(start)


for edges in edgeList:
    edges.sort()

def dfs(startVal):
    global goAvailable
    stack = []
    stack.append(startVal)

    while stack:
        item = stack.pop()
        for nextItem in reversed(edgeList[item]):
            if(areaStatus[nextItem - 1] == '0'):
                stack.append(nextItem)
            else:
                if(nextItem == startVal):
                    continue
                goAvailable += 1


for i in range(1, caseCnt + 1):
    if(areaStatus[i - 1] == '0'):
        continue
    dfs(i)


print(goAvailable)