# 9개 중 7개를 고르는 것보다
# 100을 만드는데 망칠 여지가 있는 2개를 고르는대로 빼고 출력하는 방법
# 와 이렇게 생각 할 수가 있나

arr = [0] * 9
sum = 0

for i in range(9):
    arr[i] = int(input())
    sum += arr[i]

isFounded = False

for i in range(0, 8):
    for j in range(i + 1, 9):
        if (arr[i] + arr[j] == sum - 100):
            arr[i] = 100
            arr[j] = 100
            isFounded = True
            break
    if(isFounded):
        break

sortedArr = sorted(arr, reverse=False)

for i in range(7):
    print(sortedArr[i])