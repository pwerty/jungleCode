from sys import stdin

def reversePrint(printTarget):
    for i in range(2, -1, -1):
        print(printTarget[i], end="")

inputA, inputB = input().split()


if int(inputA[2]) > int(inputB[2]):
        reversePrint(inputA)
elif int(inputA[2]) < int(inputB[2]):
        reversePrint(inputB)
else:
       if int(inputA[1]) > int(inputB[1]):
            reversePrint(inputA)
       elif int(inputA[1]) < int(inputB[1]):
            reversePrint(inputB)
       else:
            if int(inputA[0]) > int(inputB[0]):
                reversePrint(inputA)
            elif int(inputA[0]) < int(inputB[0]):
                reversePrint(inputB)
           