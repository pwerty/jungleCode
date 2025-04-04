Arr = [0] * 1000001

Arr[1] = 1
Arr[2] = 2
Arr[3] = 3

for i in range(4, 1000001):
    Arr[i] = (Arr[i - 1] + Arr[i - 2]) % 15746

num = int(input())
result = Arr[num] 
print(str(result))