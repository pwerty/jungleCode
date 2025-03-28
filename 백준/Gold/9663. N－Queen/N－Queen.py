# 퀸은 8방향 어디든 갈 수 있으니 이에 대한 처리가 필요하다.
    # 1. 퀸을 놓으려고 할 때 기존에 놓아진 모든 퀸들과의 상호 확인을 한다.
    # 2. 퀸을 생성 하는 시점에서, 판에 놓을 수 있는 여부를 업데이트 한다.

queenCnt = int(input())
# 퀸의 갯수는 실제 범위와 동일하게 한다.

pos = [0] * 15
flag_line = [False] * 50
flag_5_10 = [False] * 50
flag_2_8 = [False] * 50

totalResult = 0


def installQueen(num):
    for i in range(queenCnt):
        if(not flag_line[i] and not flag_2_8[i + num] and not flag_5_10[num - i + queenCnt - 1]):
            pos[num] = i
            if(num == queenCnt - 1):
                global totalResult
                totalResult += 1
            else:
                flag_line[i] = flag_2_8[i + num] = flag_5_10[num - i + queenCnt - 1] = True
                installQueen(num + 1)
                flag_line[i] = flag_2_8[i + num] = flag_5_10[num - i + queenCnt - 1] = False

 
installQueen(0)
print(totalResult)