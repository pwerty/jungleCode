# import sys

# caseCnt = int(sys.stdin.readline())
# visitedCnt = []

# def DFS(value):
#     stack = []
#     stack.append(value)
    
#     while stack:
#         item = stack.pop()
#         nextTurn = item[2] + 1
#         if(visitedCnt[item[0]] == -1): 
#             visitedCnt[item[0]] = item[2] 
#             print("Try these : curNode, parent, visitedCount") 
#             print(f"{item[0]}, {item[1]}, {item[2]}") 
            
#             for sideItem in edgeList[item[0]]: 
#                 if(sideItem == item[1]): 
#                     print("continue process when sideItem choice parent") 
#                     continue
                
#                 if(visitedCnt[sideItem] != -1): # judge cycle when is already visited
#                     print(f"{sideItem}, ")
#                     print(f"{visitedCnt[sideItem]} 사이클 연산 시작::")
#                     print(f"{sideItem}과 {item[0]} 간의 내용")
#                     judgeValue = item[2] - visitedCnt[sideItem] + 1
#                     if(judgeValue % 2 == 1):
#                         return False
                    
#                 visitedCnt[item[0]] = item[2]
#                 stack.append([sideItem, item[0], nextTurn])
#                 print(f"{sideItem}, {item[0]}, {nextTurn} appended")
#                 print(f"status :") print(visitedCnt) 
#                 # visitedCnt에 대한 처리가 안되어있다. 
#                 return True 
            
#     for i in range(caseCnt): 
#         nodeCnt, edgeCnt = list(map(int, sys.stdin.readline().strip().split()))
#         edgeList = [[] for _ in range(nodeCnt + 1)]
#         visitedCnt = [-1] * (nodeCnt + 1)
#         for j in range(edgeCnt): 
#             edgeStr, edgeEnd = list(map(int, sys.stdin.readline().strip().split()))
#             edgeList[edgeStr].append(edgeEnd)
#             edgeList[edgeEnd].append(edgeStr) # 다 넣으면 정렬
#             for edges in edgeList:
#                 edges.sort() 
                
#             judgeGraph = True
#             judgeGraph = DFS([1, 1, 1]) 
#             for a in range(1, len(edgeList)): 
#                 print(str(a) + "is a!!") 
#                 judgeGraph = DFS([a, a, 1]) 
                
#                 if(judgeGraph): 
#                     print("GO") 
#                 else: 
#                     print("NO") 

# TQ

from collections import defaultdict, deque
import sys

def sol():
    vertex, edge = map(int, sys.stdin.readline().split())
    color = [0] * (vertex + 1)
    series = defaultdict(list)

    for _ in range(edge):
        a, b = map(int, sys.stdin.readline().split())
        series[a].append(b)
        series[b].append(a)

    for i in range(1, vertex + 1):
        if color[i]:
            continue

        color[i] = 1

        q = deque([i])
        while q:
            item = q.popleft()
            nextClr = color[item] % 2 + 1

            for next in series[item]:
                if not color[next]:
                    color[next] = nextClr
                    q.append(next)
                elif color[next] != nextClr:
                    return "NO"
                
    return "YES"

k = int(sys.stdin.readline())
for _ in range(k):
    print(sol())