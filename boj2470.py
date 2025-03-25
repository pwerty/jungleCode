import sys

    # 양수나 음수 쪽 배열에서 아이템을 하나 잡고 남은 한쪽에서 제일 적절한 수를 찾는데 의의를 갖는다..
        # 예를 들어 -2 입장에서 3 4 5 6 7 8 9를 찾아야하면 당연히 찾을 값은 2가 될 것이다.
        # 그럼 양수 입장에서 2를 찾는 이분 탐색을 시도 하는 것이다.
        # 3 4 5 [6] 7 8 9는 너무 크니 범위를 줄인다.
        # 3 4 5 6
        # 3 [4] 5 6 여전히 크다.
        # 3
        # [3] 3은 여전히 크고 찾을 수는 없었다. 하지만 찾고자하는 2에는 제일 가깝다.
        # 보통의 이분 탐색이라면 검색 실패지만 유사 치를 찾는 것이니 이건 제일 적절하다.

        # 이런식으로 음수에서 값을 pick 한다음 가장 적합한 값을 찾는다.
        # 0에 가까운 경우는 음수, 양수, 값 순으로 값을 갱신하고 값을 기준으로 이 튜플이 변경되도록 한다.
        # 마지막엔 음수, 양수 순으로 출력하고 프로그램이 끝난다.
        



caseCnt = int(sys.stdin.readline())
numField = list(map(int, sys.stdin.readline().strip().split()))[:caseCnt]
onlyPlus = []
onlyMinus = []

ansPlus = 0
ansMinus = 0
ans = 1000000000

def binarySearch(str, end, target):
    lastestVisited = 0

    while(str <= end):
        mid = (str + end) // 2
        
        if(onlyPlus[mid] == target):
            lastestVisited = onlyPlus[mid]
            return lastestVisited

        if(onlyPlus[mid] > target):
            end = mid - 1
        else:
            str = mid + 1
        lastestVisited = onlyPlus[mid]

    if(str > end):
        return lastestVisited

numField.sort()

for i in range(len(numField)):
    if(numField[i] > 0):
        onlyPlus.append(numField[i])
    else:
        onlyMinus.append(numField[i])

if(len(onlyMinus) == 0):
    ansMinus = onlyPlus[0]
    ansPlus = onlyPlus[1]
    ans = ansMinus + ansPlus
elif (len(onlyPlus) == 0):
    ansPlus = onlyMinus[len(onlyMinus) - 1]
    ansMinus = onlyMinus[len(onlyMinus) - 2]
    ans = abs(ansMinus + ansPlus)
else:
    for i in range(len(onlyMinus)):
    # 음수 하나 픽, 이거에 제일 적합한 음수 찾기.
    # 어쨌든 이분 탐색은 제일 가까운 답을 뱉게 된다.
        targetNum = -1 * onlyMinus[i]
        expectedNum = binarySearch(0, len(onlyPlus) - 1, targetNum)
        tmpAns = abs(targetNum - expectedNum)
        if(ans > tmpAns):
            ans = tmpAns
            ansMinus = onlyMinus[i]
            ansPlus = expectedNum
    # 그 답과 더해서 나온 값이 최저치라면, 답을 갱신해야한다.
    # 답의 저장 양식은 3개이다 : ansPlus, ansMinus, ans


    # 문제 :
    # minus가 아예 없거나 plus가 아예 없는 경우를 고려해야한다.

    for i in range(len(onlyPlus) - 1):
        tmpMin = onlyPlus[i]
        tmpMax = onlyPlus[i + 1]
        tmpAnswer = abs(tmpMin + tmpMax)
        if(ans > tmpAnswer):
            ans = tmpAnswer
            ansMinus = tmpMin
            ansMax = tmpMax

    for i in range(len(onlyMinus) - 1, 1, -1):
        tmpMin = onlyMinus[i - 1]
        tmpMax = onlyMinus[i - 2]
        tmpAnswer = abs(tmpMin + tmpMax)

        if(ans > tmpAnswer):
            ans = tmpAnswer
            ansMinus = tmpMin
            ansMax = tmpMax

print(f"{ansMinus} {ansPlus}")