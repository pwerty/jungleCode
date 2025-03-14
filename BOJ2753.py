# what is 윤년
# 1차 조건 : 4의 배수
    # 2차 조건 : 100의 배수가 아닐 때 또는 400의 배수 일 때
# 1차 조건은 반드시 만족해야 하고, 2차 조건은 둘 중 하나만 만족하면 된다.
# (year % 4 == 0 AND (year % 100 != 0 OR year % 400 == 0))

year = int(input())

if (year % 4 == 0) and ((year % 100) != 0 or (year % 400 == 0)):
    print("1")
else:
    print("0")
