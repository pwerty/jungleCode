arrCnt, findNum = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))[:arrCnt]
foundCnt = 0

def func(k, result):
    global foundCnt

    if k == arrCnt:
        if(result == findNum):
            foundCnt += 1
        return
    
    func(k + 1, result + arr[k])
    func(k + 1, result)

func(0, 0)

if(findNum == 0):
    foundCnt -= 1
    
print(foundCnt)