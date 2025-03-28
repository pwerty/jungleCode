import queue
import sys

n = int(sys.stdin.readline())
field = [[0 for col in range(n)] for row in range(n)]


#isVisited F, isDrowned T
    # 방문하지 않았고 기본 값은 물에 잠긴 상태이다.
#isVisited F, isDrowned F
    # 존재 할 수 없는 상황

#isVisited T, isDrowned T
    # 방문을 통해 측정을 하였으나 rainValue 보다 낮아서 확실히 물에 잠긴 곳
#isVisited T, isDrowned F
    # 방문을 통해 측정하니 물이 잠기지 않은 곳
maxRain = 0
maxAliveFieldCnt = 0

for i in range(n):
        field[i] = list(map(int, sys.stdin.readline().strip().split()))[:n]

for i in range(n):
    for j in range(n):
        maxRain = max(maxRain, field[i][j])

for rainValue in range(1, maxRain + 1):
        # BFS
        isDrowned = [[True for col in range(n)] for row in range(n)]
        # 기본은 잠겨있는 상태이며, 실 데이터를 비교해서 잠기지 않은 곳을 구분 할 생각

        isVisited = [[False for col in range(n)] for row in range(n)]
        # 측정을 끝낸 내용에 대해 해당 됨

        # 나중에 여기서 is 계열들의 배열을 초기화 해줘야 한다.
        # 전 범위 때문에 이상이 가선 안됨
        NotDrownedFieldCnt = 0
        for i in range(n):
                for j in range(n):
                        if isVisited[i][j] == True:
                                continue
                        else:
                            if field[i][j] < rainValue:
                                    # 물에 잠기는 애들을 구분하기
                                isDrowned[i][j] = True
                                isVisited[i][j] = True
                                    #  사실 의미는 없음
                            else:

                                que = queue.Queue()
                                isDrowned[i][j] = False
                                isVisited[i][j] = True
                                que.put((i, j))
                                dx = [-1, 1, 0, 0]
                                dy = [0, 0, -1, 1]

                                while not que.empty():
                                     targetValue = que.get()
                                     for k in range(4):
                                         tmpX = targetValue[0] + dx[k]
                                         tmpY = targetValue[1] + dy[k]

                                         if(tmpX >= n or tmpX < 0 or tmpY >= n or tmpY < 0):
                                                continue
                                                # 범위 이상을 벗어나면 더 활용 할 가치가 없다.

                                         if(isVisited[tmpX][tmpY] == True):
                                                continue
                                            
                                         # 어쨌든 여기까지 오면 다음 사항들이 해당 된다 :
                                             # tmpX와 tmpY 는 field의 정상 범위 내에 있다.
                                             # isVisited이 False라서 측정 기록이 없다.

                                         if(field[tmpX][tmpY] >= rainValue):
                                                # 물에 안잠기는거 맛죠?
                                                isDrowned[tmpX][tmpY] = False
                                                isVisited[tmpX][tmpY] = True

                                                que.put((tmpX, tmpY))
                                         else:
                                                isDrowned[tmpX][tmpY] = True
                                                isVisited[tmpX][tmpY] = True
                                # 여기까지 오면 상하좌우에 대해 모두 조사는 한거니까
                                # else로 빠진 것부터 최소 한칸이 있는 거니까
                                # 물에 잠기지 않은 유의미 한 값이 있다는게 된다.
                                NotDrownedFieldCnt += 1
        maxAliveFieldCnt = max(maxAliveFieldCnt, NotDrownedFieldCnt)


                                        
                                        

                                                                                     
print(str(maxAliveFieldCnt))