import sys
input = sys.stdin.readline


# 3 - 4 , 1 - 2, 7 - 6 - 5?
# 그럼 3 시작을 찍고 4 1 2를 갈 수 없다. 당연한거긴 한데..

# 내가 가는 길이 조건에 부합하지 않은 ending route라는걸 인지하는 방법
    # 3 4 [5]에 왔는데 다 들른게 아니라서 갈 수 없어요 : 근데 직전 칸이었던 4를 와버렸으니 이제 5에 가려면 6에서부터 와야하는 상태를 인지하고 있어요
    # 그러면 마지막은 반드시 7이 되어야하는데 그러면 마지막이 7로 결정되었기 때문에 그 전에 방문해야할 곳은 3 4와 7 6 5를 제외한 1 2가 되네요 이걸 어떻게코드로 만듦?

    # 공책 동원
    # 1이나 N이 시작점이고, 1-N 사이에 End가 있으면 답 : 1
    # 1이나 N이 시작점이고, 끝 점이 다른 하나이면 답 : 0
    # 1-N 사이에 End가 있고 또 시작점도 범위내라면
        # End의 nearby에 시작점이 있는지 확인. 1 2 3 4 [5] 6 7 8 9 라고 하면 4, 6이 시작점인지 봐야함
            # 해당하면, 답 : 2
            # 해당하지 않으면, 답 : 3
numCnt = int(input())
for i in range(numCnt):
    mazeSize, mazeStr, mazeEnd = numList = list(map(int, sys.stdin.readline().split()))

    if(mazeStr == mazeSize and mazeEnd == 1):
        print("0")
        continue

    if(mazeStr == 1 and mazeEnd == mazeSize):
        print("0")
        continue

    if(mazeStr == 1 or mazeStr == mazeSize):
        print("1")
        continue

    # 여기까지 오면 mazeStr이 1, N인경우는 없음
    if(mazeEnd - 1 == mazeStr or mazeEnd + 1 == mazeStr):
        print("1")
        continue
        
    print("2")
    continue
        
    

