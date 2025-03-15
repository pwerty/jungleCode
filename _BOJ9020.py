from math import sqrt
from sys import stdin

array = list(range(1, 10001))
squareRoot = sqrt(10000)


for i in range(int(squareRoot)):
    if i == 0 or i == 1:
        continue
    isNotPrime = False
    for j in range(2, i):
        # range가 i라는건 어쨌든 i - 1 까지인거니까 의미있는 소수 판정이 가능하다
        if i % j == 0:
            isNotPrime = True

        if isNotPrime:
            break
        # i라는 숫자 하나에 대해 모든 숫자를 대조해서 비교하니, 
        # 중간에 소수가 아님이 확인된다면 바로 그만 둘 수 있도록 한다.
    
    # 이쪽 영역에 들어오면 백프로 소수이다.
    for j in range(2, (int(squareRoot) // i) + 1):
        # squareRoot 숫자를 넘어가지 않도록 하기 위함이다. 즉 i가 7이면 sqR // i는 14가 나오겠지, 하지만 range는 해당 숫자 직전에서 끝내기 때문에
        # + 1을 끝 점에 지정한다. 그리고 * 1 이 계산되면 안되기때문에 명시적으로 2를 적는다.
        delTargetIdx = i * j - 1
        array[delTargetIdx] = -1
        # array[0] = 1이 들어있으니, 내가 뺴야하는 값에서 - 1을 해야 빼야하는 값의 위치가 잡힌다.

# 이거 array가 어쨌든 길이가 가변성이니 문제가 생길 수 있겠다.
a = 0
while a < len(array):
    if array[a] == -1:
        del array[a]
    else:
        a += 1

# 여기서 모든 소수 목록의 결과를 확인 할 수 있다.
# 에라토스 뭐시기의 체는 구현 완료

# 그럼 소수만 있는 Pool에서 전개를 해나가야한다.
# 입력된 숫자의 범위 이상 직전
    # 즉 8이 입력되면 8은 소수 7보다 크고 소수 11보다 작으니 7까지의 범위를 제한하고
    # 여기서 더해질 수 있는 모든 쌍을 얻어야한다.
    # 쌍을 얻고나면 두 차가 제일 작은 경우가 답이 된다.

caseNum = int(stdin.readline())


for i in range(caseNum):
    resultList = []
    minVal = 10000000
    minIdx = 0

    targetNum = int(stdin.readline())
    isFounded = False
    defIdx = 0

    for j in range(len(array)):
        # targetNum이랑 비교해서 범위를 찾아내야한다.
        if targetNum <= array[j]:
            isFounded = True
            defIdx = j - 1
            break
    
    for j in range(defIdx):
        for k in range(defIdx):
            if targetNum == array[j] + array[k]:
                resultList.append([array[j],array[k]])

    for idx, pair in enumerate(resultList, start=0):
        result = abs(pair[0] - pair[1])

        if minVal > result:
            minVal = result
            minIdx = idx
    
    print(str(resultList[minIdx][0]) + " " + str(resultList[minIdx][1]))


    # 체를 먼저 구해놓고 하려 했는데 안되네
    # 여기서 시간 절약 할 방법이 있을까?

    # 입력을 전부 받고 최대값에 해당하는 값까지만 체를 밝혀놓기?