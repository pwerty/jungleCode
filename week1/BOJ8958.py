# 가중점수 개념
testCaseCnt = int(input())

for i in range(testCaseCnt):
    testCase = input()
    scoreAddVal = 0
    totalScore = 0
    for j in range(len(testCase)):
        if testCase[j] == 'O':
            scoreAddVal += 1
            totalScore += scoreAddVal
        else:
            scoreAddVal = 0

    print(str(totalScore))