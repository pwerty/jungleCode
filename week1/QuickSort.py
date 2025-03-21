import sys

# 미완성
# pivot을 우선 지정한다
# 사용 할 변수는 left right (전체 범위에 대한 지정), i j (인덱스로써 배열 전체를 순환하는 역할)
arr = [5, 2, 7, 3, 8, 9, 6]

# pivot이 있어야 할 정확한 위치를 지정해야한다.
    # pivot이 위치한 곳 좌측에는 pivot의 content 보다 적은 숫자, 우측에는 pivot보다 큰 숫자가 오게끔 하는 요구조건이 있다.
    # 그렇다면 i j가 순환하는 동안 pivot과 값 비교를 해서 값 순환이 필요한 시점이 필요 할 수 있다.

def quickSort(sortTarget, left, right):
    i = left
    j = right
    pivot = (i + j) // 2

    while i <= j:
        is_i_Ready = False
        is_j_Ready = False

        if sortTarget[i] < sortTarget[pivot]:
            is_i_Ready = True
        else:
            i += 1
            continue

        if sortTarget[j] >= sortTarget[pivot]:
            is_j_Ready = True
        else:
            j -= 1
            continue

        if(is_i_Ready and is_j_Ready):
            swap(sortTarget, i, j)
            i += 1
            j -= 1

    if i >= j:
        print(arr)
        print("다음 정리 시작!!!")
        print("------------------------")
        quickSort(sortTarget, left, i - 1)
        quickSort(sortTarget, i + 1, right)


def swap(arr, targetStr, targetDest):
    a = arr[targetStr]
    arr[targetStr] = arr[targetDest]
    arr[targetDest] = a

    # 5 2 7 3 8 9 6

quickSort(arr, 0, len(arr) - 1)
print(arr)