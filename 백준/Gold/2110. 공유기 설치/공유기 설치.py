import sys

fieldCnt, routerCnt = list(map(int, sys.stdin.readline().strip().split()))
field = []

for i in range(fieldCnt):
     field.append(int(sys.stdin.readline()))

field.sort()
minPos = field[0]
maxPos = field[len(field) - 1] - minPos

def func(installed, curTouchedIdx, distVal):
    if(installed == routerCnt):
         return True
    
    for i in range(curTouchedIdx + 1, len(field)):
         if(field[i] - field[curTouchedIdx] >= distVal):
              isFound = func(installed + 1, i, distVal)
              if(isFound):
                   return True
    return False

def binarySearch(start, end):
     result = 0
     installedCnt = 1
     areFound = False
     
     while (start <= end):
          mid = (start + end) // 2
          for i in range(1, len(field)):
               if(field[i] - field[0] >= mid):
                    areFound = func(installedCnt + 1, i, mid)

                    if(areFound):
                         break

          if areFound is True:
               result = mid
               start = mid + 1
               # 찾은 상황에선 수치를 전체적으로 올린다가 아닌거같은데
          else:
               end = mid - 1
               # 찾지 못했다면 수치를 전체적으로 내린다

     return result
               

def isFeasible(distVal):
    installedCnt = 1
    lastInstalled = field[0]

    for i in range(1, len(field)):
        if field[i] - lastInstalled >= distVal:
            installedCnt += 1
            lastInstalled = field[i]
            if installedCnt >= routerCnt:
                return True

    return False

# 이분 탐색 함수
def bSearch(start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if isFeasible(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result
               
    

print(f"{bSearch(1, maxPos)}")