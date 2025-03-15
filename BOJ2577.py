inputA = int(input())
inputB = int(input())
inputC = int(input())

target = inputA * inputB * inputC
target = str(target)
array = [0] * 10


for i in range(len(target)):
    array[int(target[i])] += 1

for i in range(10):
    print(str(array[i]))