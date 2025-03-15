inputNum = int(input())
hansuCnt = 0

for i in range(1, inputNum + 1):
    if i < 100:
        hansuCnt += 1
    else:
        _t100 = i // 100
        _t10 = i // 10 % 10
        _t1 = i % 10

        if _t100 - _t10 == _t10 - _t1:
            hansuCnt += 1

print(hansuCnt)
