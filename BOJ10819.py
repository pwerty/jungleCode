caseCnt = int(input())
arr = list(map(int, input().strip().split()))[:caseCnt]
ansArr = []
selected = [-1] * 8
maxValue = 0
cnt = 0

def func(selectArr, choiceNum):
    global maxValue, cnt

    # 모든 selectArr이 선택된 경우 출력하고 탈출
    if choiceNum == caseCnt + 1:
        total = 0
        for i in range(1, caseCnt):
            # 실제 인덱스를 가리킬 내용 selected[i]
            total += abs(arr[selected[i - 1] - 1] - arr[selected[i] - 1])
            # 여기서 이제 최대를 비교해서 갱신 하면 된다.
        cnt += 1
        if maxValue < total:
            maxValue = total
            ansArr.clear()
            for i in range(0, caseCnt):
                 ansArr.append(arr[selected[i] -  1])
            return

    # 모든 selectArr이 선택되진 않은 경우, 
    # 비어 있는 내용을 찾아본다.
    for i in range(caseCnt):
        if selectArr[i] != -1 :
            continue
        else:

            selectArr[i] = choiceNum
            func(selectArr, choiceNum + 1)
            selectArr[i] = -1



for i in range(caseCnt):
    
    selected[i] = 1
    func(selected, 2)
    selected[i] = -1
        
print(str(maxValue))