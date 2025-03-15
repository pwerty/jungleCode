# 테스트 케이스 받고

    # 한 테스트 케이스의 내용물 : 학생 수, 학생 수 만큼의 내용
    # 모든 인원의 점수를 받고 평균을 낸다. 그 평균을 모든 인원을 확인해서 평균 이상 여부를 세어본다.
    # 그리고 (평균 이상인 사람 수) / (전체 인원 수) 하면 0.4던 0.6이건 나오겠지, 이걸 퍼센테이지로 출력 되게끔 전환한다.

# 모든 테스트 케이스 통과까지 반복한다.

testCaseCnt = int(input())

for i in range(testCaseCnt):
    scoreList = list(map(int, input().strip().split()))
    studentCnt = scoreList[0]
    del scoreList[0]
    scoreTotal = 0
    scoreAvge = 0
    for j in range(studentCnt):
        scoreAvge += scoreList[j]

    scoreAvge /= studentCnt
    afterAvgeCnt = 0

    for j in range(studentCnt):
        if scoreAvge < scoreList[j]:
            afterAvgeCnt += 1

    ansVal = round(((afterAvgeCnt / studentCnt)) * 100, 3)
    formattedNum = "{:.3f}".format(ansVal)
    print(str(formattedNum) + "%")