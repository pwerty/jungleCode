# 쿼드 트리랑 내용이 똑같네
lineLength = int(input())
field = [list(map(int,input().strip().split())) for _ in range(lineLength)]
colorCnt = [0, 0]

def func(m, x, y):
    isDiff = False
    pivotValue = field[x][y]
    if(m == 0):
        colorCnt[pivotValue] += 1
        return


    for i in range(x, x + (2 ** m)):
        for j in range(y, y + (2 ** m)):
            if(field[i][j] != pivotValue):
                isDiff = True
            
            if(isDiff):
                break

        if(isDiff):
            break
    
    if(isDiff):
        func(m-1, x, y)
        func(m-1, x + (2 ** (m - 1)), y)
        func(m-1, x, y + (2 ** (m - 1)))
        func(m-1, x + (2 ** (m - 1)), y + (2 ** (m - 1)))
                                           
                                           
    else:
        colorCnt[pivotValue] += 1
        return

# input 구성하고, 제곱 수 만드는 방법 생각해두기

tmpVal = lineLength
multipleVal = 0
while tmpVal != 1:
    multipleVal += 1
    tmpVal = tmpVal // 2

func(multipleVal, 0, 0)

print(colorCnt[0])
print(colorCnt[1])
