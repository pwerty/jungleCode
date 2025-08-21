import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(0, n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x: x[0])
prevHeight = 0
answer = 1

prev = arr[0]

for i in range(1, n):
    # 같거나 작으면 같이 넘어지니 ok, 크면 안됨
    cur = arr[i]

    if(prev[0] + prev[1] < cur[0]):
        answer += 1
    prev = cur
        
    #같이 넘어지는 해당이 있는경우, 다다음이 넘어지게끔 넘어가는걸 조정해야해요

print(answer)