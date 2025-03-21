
targetNum = int(input())

# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

# 주어진 수가 10보다 작다면 0을 왼쪽에 추가 해서 두 자리 수로 만들고, 두 자리의 계수를 더한다.
# 그 다음에 주어진 수의 1의 자리, 그리고 위에서 구한 합의 1의 자리를 이어 붙이면 새로운 수를 만들 수 있다.

if targetNum >= 0:
    
    cycleCount = 0
    # 주어진 수가 10보다 클 때 이 코드가 실행된다.
    _n1 = targetNum % 10
    _n10 = targetNum // 10
    # 각 자리를 나눈다.

    newTarget = _n1 + _n10
    # 나눈 내용끼리 합한다.
    newTarget = newTarget % 10
    # 나눈 내용을 합한 내용의 오른쪽 자리수를 사용 해야한다.
    newTarget = newTarget + (_n1 * 10)
    # _n1은 주어진 수의 오른쪽 자리를 의미한다. 그러니 이 코드는 나눈 내용을 합한 내용의 오른쪽 자리수와 주어진 수의 오른쪽 자리이다.
    cycleCount += 1
    while (newTarget != targetNum):
            _n1 = newTarget % 10
            _n10 = newTarget // 10

            newTarget = _n1 + _n10
            # 나눈 내용끼리 합한다.
            newTarget = newTarget % 10
            # 나눈 내용을 합한 내용의 오른쪽 자리수를 사용 해야한다.
            newTarget = newTarget + (_n1 * 10)
            # _n1은 주어진 수의 오른쪽 자리를 의미한다. 
            # 그러니 이 코드는 나눈 내용을 합한 내용의 오른쪽 자리수와 주어진 수의 오른쪽 자리이다.

            cycleCount += 1
    
    print(str(cycleCount))
