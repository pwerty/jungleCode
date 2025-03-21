score = int(input())

scoreTracker = score // 10


if scoreTracker >= 9:
    print("A")
elif scoreTracker == 8:
    print("B")
elif scoreTracker == 7:
    print("C")
elif scoreTracker == 6:
    print("D")
else:
    print("F")

