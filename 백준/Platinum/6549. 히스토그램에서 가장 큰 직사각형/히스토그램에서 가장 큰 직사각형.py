import sys





def calcHisto(L, R):
    if L > R:
        return 0  # 예외 처리
    if L == R:
        return histogram[L]  # 단일 요소 반환

    mid = (L + R) // 2
    Lmax = calcHisto(L, mid - 1)  # 좌측 최대값
    Rmax = calcHisto(mid + 1, R)  # 우측 최대값
    # 중앙 구간 최대값 계산
    midToL = mid
    midToR = mid
    low_tall = histogram[mid]
    Mmax = low_tall

    while midToL > L or midToR < R:
        # 왼쪽 또는 오른쪽으로 확장
        if midToL > L and (midToR == R or histogram[midToL - 1] >= histogram[midToR + 1]):
            midToL -= 1
            low_tall = min(low_tall, histogram[midToL])
        elif midToR < R:
            midToR += 1
            low_tall = min(low_tall, histogram[midToR])

        # 좌우 확장된 구간의 최대 넓이 계산
        Mmax = max(Mmax, low_tall * (midToR - midToL + 1))

    # 최댓값 반환
    return max(Lmax, Rmax, Mmax)



    # 왼쪽 확장
    while midToL > L:
        min_tall = min(min_tall, histogram[midToL])
        tmp = (mid - midToL + 1) * min_tall
        Mmax = max(Mmax, tmp)
        midToL -= 1

    # 오른쪽 확장
    midToR = mid
    min_tall = histogram[mid]  # min_tall 초기화
    while midToR < R:
        midToR += 1
        min_tall = min(min_tall, histogram[midToR])
        tmp = (midToR - mid + 1) * min_tall
        Mmax = max(Mmax, tmp)

    # 최댓값 반환
    return max(Lmax, Rmax, Mmax)


isContinue = True

while isContinue:

    histogram = list(map(int, sys.stdin.readline().strip().split()))
    cnt = histogram[0]
    if(cnt == 0):
        isContinue = False
        continue
    histogram.remove(cnt)
    print(calcHisto(0, len(histogram) - 1))


