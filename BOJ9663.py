
# N queen
import sys

sys.setrecursionlimit(2000)

# 퀸은 8방향 어디든 갈 수 있으니 이에 대한 처리가 필요하다.
    # 1. 퀸을 놓으려고 할 때 기존에 놓아진 모든 퀸들과의 상호 확인을 한다.
    # 2. 퀸을 생성 하는 시점에서, 판에 놓을 수 있는 여부를 업데이트 한다.

queenCnt = int(input())
# 퀸의 갯수는 실제 범위와 동일하게 한다.

array = [[0 for col in range(16)] for row in range(16)]
totalResult = 0
# 0은 놓아진 게 없음, 1은 퀸이 설치되었음, 2는 퀸을 설치 할 수 없음으로 하자.

def queenInstaller(array, _x, _y):
    
    if array[_x][_y] != 0:
        # 배치가 가능한지를 기본적으로 확인해야한다.
        #print("install failed! tried axis is : " + str(_x) + " , " + str(_y))
        return
    # 배치가 가능하다면 배치를 한다.
    array[_x][_y] = 1
    #print("installed in " + str(_x) + " " + str(_y))

    if(_x + 1 == queenCnt):
        # 정한 갯수만큼 설치 했다면 거기서 중단 할 수 있다.

        #print("FULL INSTALL COMPLETED!")
        #for a in range(0, 10):
            #for b in range(0, 10):
                #print(str(array[a][b]), end="")
            #print("")
        global totalResult
        totalResult += 1
        return

    # 배치 금지 구역을 새롭게 설정해야한다.
    for i in range(queenCnt):
        if(_x + i >= queenCnt) or (_y + i >= queenCnt):
            c = 0
        else:
            if(array[_x + i][_y + i] == 0):
                array[_x + i][_y + i] = 2
            #print("blocked " + str(_x + i) + " " + str(_y + i))

            # 남동
        if(_x - i <= 0) or (_y - i <= 0):
            c = 0
        else:
            if(array[_x - i][_y - i] == 0):
                array[_x - i][_y - i] = 2
            #print("blocked " + str(_x - i ) + " " + str(_y - i))

            # 북서
        # 북서쪽 남동쪽 가로지르는 대각선 처리

        tmpXplus = _x + i
        tmpYplus = _y + i
        tmpXminus = _x - i
        tmpYminus = _y - i

        if(tmpYplus >= queenCnt or tmpXminus < 0):
            c = 0
        else:
            if(array[tmpXminus][tmpYplus] == 0):
                array[tmpXminus][tmpYplus] = 2
                #print("blocked " + str(tmpXminus) + " " + str(tmpYplus))

        if(tmpXplus >= queenCnt or tmpYminus < 0):
            c = 0
        else:
            if(array[tmpXplus][tmpYminus] == 0):
                array[tmpXplus][tmpYminus] = 2
                #print("blocked " + str(tmpXplus) + " " + str(tmpYminus))

        
            # 북동쪽과 남서쪽 가로지르는 대각선 처리

        if(array[_x][i] == 0):
           array[_x][i] = 2
        
        if(array[i][_y] == 0):
            array[i][_y] = 2

    
    for j in range(0, queenCnt):
        local_array = [row[:] for row in array]
        queenInstaller(local_array, _x + 1, j)
        # _x 기반으로 움직이게끔 한다. 즉 다음 작동은 
        # 기존 _x 다음줄로 항상 진행되고, _y 가 순차적으로 움직이며 배치를 시도한다.
        # 그럼 결과적으로 _x가 놓는데 성공한 갯수가 된다. 결국 같은 열에선 이뤄 질 수 없으니까
        # 다만 이 설치가 성공한 시점에서 갯수를 세어보고 맞다면 거기서 해당 과정을 중단 할 수 있다.


for i in range(0, queenCnt):
   # print("starting install from " + str(0) + " " + str(i))
    local_array = [row[:] for row in array]
    queenInstaller(local_array, 0, i)

print(totalResult)

 