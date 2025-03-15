# 그냥 머지소트 하나 생각해서 1, 2, 3 다 패싱 하려고~
itemCnt = int(input())
array = []
sorted = [0] * itemCnt

for i in range(itemCnt):
    array.append(int(input()))

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if(arr[i] < arr[j]):
            sorted[k] = arr[i]
            k += 1
            i += 1
        else:
            sorted[k] = arr[j]
            k += 1
            j += 1

    if i > mid:
        # 왼쪽이 다 털린거니까 오른쪽 털기
        for a in range(j, right + 1):
            sorted[k] = arr[a]
            k += 1
    else:
        # 오른쪽이 다 털린거니까 왼쪽 털기
        for a in range(i, mid + 1):
            sorted[k] = arr[a]
            k += 1

    for i in range(left, right + 1):
        arr[i] = sorted[i]


def mergeSort(arr, str, end):
    if(str < end):
        mid = (str + end) // 2
        mergeSort(arr, str, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, str, mid, end)

mergeSort(array, 0, len(array) - 1)

for i in range(len(array)):
    print(array[i])