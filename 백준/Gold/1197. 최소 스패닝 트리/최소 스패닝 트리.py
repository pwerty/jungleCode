import sys

totalNodes, edgeCnt = list(map(int, sys.stdin.readline().strip().split()))
edgeList = []
sortedList = []
parent = [0] * (totalNodes + 1)
rank = [0] * (totalNodes + 1)
compCount = totalNodes

for i in range(1, totalNodes + 1):
    parent[i] = i

for i in range(edgeCnt):
    inputA, inputB, cost = list(map(int, sys.stdin.readline().strip().split()))
    edgeList.append([inputA, inputB, cost])

sortedList = sorted(edgeList, key=lambda x: x[2])

def find(item):
    if(parent[item] == item):
        return item
    else:
        return find(parent[item])

def union(itemA, itemB):
    global compCount
    compA = find(itemA)
    compB = find(itemB)
    


    if(compA == compB):
        return False
    
    compCount -= 1
    if(rank[compA] > rank[compB]):
        parent[compB] = compA
    elif rank[compB] > rank[compA]:
        parent[compA] = compB
    else:
        parent[compB] = compA
        rank[compA] += 1
    return True

cnt = ans = 0
for i in range(len(sortedList)):
    

    if not union(sortedList[i][0], sortedList[i][1]):
        continue
    ans += sortedList[i][2]
    cnt += 1
    if(cnt == totalNodes - 1):
        break
print(ans)

