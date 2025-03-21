import sys

sys.setrecursionlimit(10**8)
cityCnt = int(sys.stdin.readline())
field = [[0 for col in range(cityCnt)] for row in range(cityCnt)]

for i in range(cityCnt):
    field[i] = list(map(int, sys.stdin.readline().strip().split()))[:cityCnt]

# 내가 구상한 방식
    # 어쨌든 비용에 대한 행렬을 초반에 모두 입력 받기로 한다.
    # 갈 수 없는 경우는 0이 주어지는데 그러면 0을 발견하는 경우 그냥 지나갈 수 있게 만든다.

    # city count가 3인데 이렇게 된 배열이 존재한다고 하자.
    # 0 1 1 : 1번 도시에서 각 도시로 가는건 모두 1원이다.
    # 1 0 9 : 2번 도시에서 1번 도시로 가는건 1원, 3번 도시로 가는건 9원이다.
    # 9 9 0 : 3번 도시에서 각 도시로 가는건 모두 9원이다.

    # 어쨌든 3번 도시의 비용은 필수 불가결하지만
    # 2번 도시 입장에서 1번으로 다시 돌아간다음 3번을 선택할 여지는 충분히 있다.

    # 그렇다는 것은 자기 자신에 대한 방문 여부는 시작부터 찍어선 안된다는 이야기가 된다.
    # 차라리 0에 대한 masking이 작성에 대해 더 유연하게 반응 될 수 있을 것 같다.

    # 원래 이야기로 돌아와서, 그러면 selected에 대한 콜을 다시 만들되 10개의 콜을 쓰는 방식으로 작성해야한다.

selected = [-1] * cityCnt
minValue = 1000000000000

def func(selectArr, choiceNum, lateVisited):
    global minValue

    # 모든 selectArr이 선택된 경우 출력하고 탈출
    if choiceNum == cityCnt:
        total = 0
        for i in range(0, cityCnt):
            # 실제 인덱스를 가리킬 내용 selected[i]
            if(field[i][selectArr[i]] == 0):
                return
            total += field[i][selectArr[i]]
            
            # i번째 인덱스에 담겨있는 contents : selected[i]
            # 즉, 출발지는 i이고 도착지는 selected[i] - 1 이다.
            # 전부 더한 뒤 최소 여부를 확인 후 갱신하기로 하자.
        
        if minValue > total:
            minValue = total
            return

    # 모든 selectArr이 선택되진 않은 경우, 
    # 비어 있는 내용을 찾아본다.
    for i in range(cityCnt):
        if field[lateVisited][i] == 0:
            continue
        
        if selectArr[i] != -1 :
            continue
        else:
            selectArr[i] = choiceNum
            func(selectArr, choiceNum + 1, i)
            selectArr[i] = -1



for i in range(cityCnt):
    # 모든 도시에서 출발 할 수 있다는 여지를 둔다.
    selected[i] = 0
    func(selected, 1, i)
    selected[i] = -1
        
print(str(minValue))