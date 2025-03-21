import sys
inputA, inputB, inputC = list(map(int, sys.stdin.readline().strip().split()))[:3]
sys.setrecursionlimit(10**8)
# 모듈러 연산의 분배 가능한 점을 이용하기
# a * b 를 mod m 하는 것은
# a mod m * b mod m * mod m 과 같다.

# 근데 여기선 inputA를 inputB 번 곱한 것을 inputC로 나눠서 출력하라고 하네.
# 그럼 a = b 이다.


def func(originNum, multiPleNum, modNum):
    if(multiPleNum <= 1):
        return originNum % modNum
    
    value = func(originNum, multiPleNum // 2, modNum)

    if multiPleNum % 2 == 0:
        return (value * value) % modNum    
    else:
        originToMod = originNum % modNum
        return (value * value * originToMod) % modNum

print(func(inputA, inputB, inputC))