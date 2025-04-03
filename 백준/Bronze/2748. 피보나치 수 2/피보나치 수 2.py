fArr = [0] * 100

fArr[0] = 0
fArr[1] = 1

for i in range(2, 91):
    fArr[i] = fArr[i - 1] + fArr[i - 2]

finding = int(input())

print(fArr[finding])