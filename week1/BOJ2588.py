inputA = 0
inputB = 0

inputA = int(input(""))
inputB = int(input(""))

_t100 = inputB // 100
_t10 = inputB // 10 % 10
_t1 = inputB % 10

print(inputA * _t1)
print(inputA * _t10)
print(inputA * _t100)

print(inputA * inputB)