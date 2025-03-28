
def facto(num):
    if num <= 1:
        return 1
    else:
        return facto(num - 1) * num
    

i = int(input())
print(facto(i))