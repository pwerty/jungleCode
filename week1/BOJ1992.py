import sys

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
def func(m, x, y):
    if(m == 0):
        print(str(arr[x][y]), end="")
        return
    
    pivotValue = arr[x][y]
    
    isDiff = False
    for i in range(x, (x + 2 ** m)):
        for j in range(y, (y + 2 ** m)):
            if(pivotValue != arr[i][j]):
                isDiff = True
                #print(str(i) + ", " + str(j) + " 에서 값 변동이 발생하여 추가 재귀 호출을 시도합니다!!")
                break
        
        if(isDiff):
            break

    if(isDiff):
        print("(", end="")
        func(m - 1, x, y)
        func(m - 1, x, y + 2 ** (m - 1))
        func(m - 1, x + 2 ** (m - 1), y)
        func(m - 1, x + 2 ** (m - 1), y + 2 ** (m - 1))
        print(")", end="")
    else:
        # 이 func를 타고 들어온뒤 isDiff에 대해 이상이 없으면 해당 영역은 일관된 수를 가지고 있다.
        print(str(pivotValue), end="")
        return


getMultipleVal = n
realValue = 0
while (getMultipleVal != 1):
    getMultipleVal //= 2
    
    realValue += 1

func(realValue, 0, 0)