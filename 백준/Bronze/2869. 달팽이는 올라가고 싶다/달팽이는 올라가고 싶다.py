from sys import stdin
from math import ceil

numList = list(map(int, stdin.readline().strip().split()))

courseLong = numList[2]
goForward = numList[0]
goBack = numList[1]
spendedDay = 1

courseLong -= goForward
courseLong = ceil(courseLong / (goForward - goBack))

print(spendedDay + courseLong)