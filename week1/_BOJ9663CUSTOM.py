# 퀸은 8방향 어디든 갈 수 있으니 이에 대한 처리가 필요하다.
    # 1. 퀸을 놓으려고 할 때 기존에 놓아진 모든 퀸들과의 상호 확인을 한다.
    # 2. 퀸을 생성 하는 시점에서, 판에 놓을 수 있는 여부를 업데이트 한다.

queenCnt = int(input())
# 퀸의 갯수는 실제 범위와 동일하게 한다.

newArray = [-1] * 16
totalResult = 0

def queenInstaller(arr, idx, installedLoc):
        # 설치 한 적 없는 곳을 보자. 배치가 가능한지를 확인해야한다.
    for i in range(idx):
        if installedLoc == arr[i]:
            return
            # 기존의 설치한거랑 열이 같은지 확인한다.
            
        if abs(i + arr[i]) == abs(idx + installedLoc):
            return
            # 기존 설치 된 아이템 중 10시 - 5시 방향 대각선을 확인해야한다.

        if (i - arr[i]) == (idx - installedLoc):
            return
            # 기존 설치 된 아이템 중 2시- 8시 방향 대각선을 확인해야한다.

    arr[idx] = installedLoc
    
    if(idx + 1 == queenCnt):
        global totalResult
        totalResult += 1
        return
    
    
    for j in range(0, queenCnt):
        queenInstaller(arr, idx + 1, j)
        # _x 기반으로 움직이게끔 한다. 즉 다음 작동은 
        # 기존 _x 다음줄로 항상 진행되고, _y 가 순차적으로 움직이며 배치를 시도한다.
        # 그럼 결과적으로 _x가 놓는데 성공한 갯수가 된다. 결국 같은 열에선 이뤄 질 수 없으니까
        # 다만 이 설치가 성공한 시점에서 갯수를 세어보고 맞다면 거기서 해당 과정을 중단 할 수 있다.
    arr[idx] = -1

for i in range(0, queenCnt):
   # print("starting install from " + str(0) + " " + str(i))
    queenInstaller(newArray, 0, i)

print(totalResult)
