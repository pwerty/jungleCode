inp=int(input())
def hanoi(x,a,b,c):
    if x == 1:
        if (inp <= 20):
            print('{} {}'.format(a,c))
    else:
        hanoi(x-1,a,c,b)
        if (inp <= 20):
            print('{} {}'.format(a,c))
        hanoi(x-1,b,a,c)
print(2** inp-1)
hanoi(inp,1,2,3)