caseNum = int(input())


for i in range(caseNum):
    repeatCnt, repeatString = input().split()
    repeatCnt = int(repeatCnt)

    for j in range(len(repeatString)):
        for k in range(repeatCnt):
            print(repeatString[j], end="")
    print()