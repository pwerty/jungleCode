
from itertools import permutations


import sys

cityCnt = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(cityCnt)]
ans = 100000000




for i in permutations(range(1, cityCnt), cityCnt-1):
    num_list = [*i]
    num_list = [0] + num_list + [0]
    sub = 0
    
    for j in range(cityCnt):
        cost = field[num_list[j] - 1][num_list[j + 1] - 1]

        if cost == 0:
            break
        else:
            sub += cost

        if sub > ans :
            break
    else:
            if ans > sub:
                ans = sub
print(ans)