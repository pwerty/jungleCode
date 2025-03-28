from sys import stdin

def isPrimeNum(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True
        

caseNum = int(stdin.readline())

for i in range(caseNum):
    targetNum = int(stdin.readline())
    targetA = targetNum // 2
    targetB = targetA


    minVal = 1000000
    minIdx = 0

    while targetA != 1:
        if isPrimeNum(targetA) and isPrimeNum(targetB):
                print(str(targetA) + " " + str(targetB))
                break

        targetA -= 1
        targetB += 1  
    


