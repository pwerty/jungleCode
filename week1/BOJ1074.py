
def getRealValue(num, multiplyCnt):
    if multiplyCnt == 0:
        return 1

    needMultiply = num
    while multiplyCnt > 1:
        num = num*needMultiply
        multiplyCnt -= 1
    return num

def goAround(oneLength, _x, _y):
    plusValue = getRealValue(2, oneLength)
    half = plusValue // 2
    if half == 1:
        if _x < half and _y < half:
            return 0 
        elif _x < half and _y >= half:
            return 1
        elif _x >= half and _y < half:
            return 2
        else:
            return 3
    else:
        if _x < half and _y < half:
            # Area 1
           return int(goAround(oneLength - 1, _x, _y)) 
        elif _x < half and _y >= half:
            # Area 2
           return int(half * half * 1 + goAround(oneLength - 1, _x, _y - half))
        elif _x >= half and _y < half:
            # Area 3
            return int(half * half * 2 + goAround(oneLength - 1, _x - half, _y))
        else:
            # Area 4
           return int(half * half * 3 + goAround(oneLength - 1, _x - half, _y - half))


oneLengthInput, inputX, inputY = input().split()
oneLengthInput = int(oneLengthInput)
inputX = int(inputX)
inputY = int(inputY)

print(goAround(oneLengthInput, inputX, inputY))

# 매개변수는 변의 길이, x 좌표, y 좌표 순으로 주고

# 길이가 1일때
    # (여기서 이야기하는 0 1은 가중치의 존재 여부만을 말함, 실제 가중치가 얼마나 되는지는 2의 제곱 상황에 따라 변동된다.
# 시작점에서 + 0 0 인경우
# 시작점에서 + 0 1 인경우 
# 시작점에서 + 1 0 인경우
# 시작점에서 + 1 1 인경우

# 길이가 1이 아니면
#     길이를 줄인 채로 다시 다음 재귀함수를 호출하게끔 하기

