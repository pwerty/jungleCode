import sys

inputA, inputB = input().split()
inputA = int(inputA)
inputB = int(inputB)
field = list(map(int, sys.stdin.readline().strip().split()))[:inputA]
ans = 0

def func(k, total):
    if(k == field.count()):
        return
    
    if(total == inputB):
        ans += 1
        return
    
    func(k + 1, total + field[k])
    func(k + 1, total)

print(ans)