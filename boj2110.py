import sys

fieldCnt, routerCnt = list(map(int, sys.stdin.readline().strip().split()))
field = []

for i in range(fieldCnt):
     field.append(int(sys.stdin.readline()))

field.sort()
minPos = field[0]
maxPos = field[len(field) - 1] - minPos

def isInstallAble(distance):
     installed = 1
     lastVisited = field[0]

     for i in range(1, len(field)):
          if(field[i] - lastVisited >= distance):
               lastVisited = field[i]
               installed += 1

               if(installed == routerCnt):
                    return True
     return False
                     
               

def binarySearch(start, end):
     result = 0
     areFound = False

     while (start <= end):
          mid = (start + end) // 2
          if isInstallAble(mid) is True:
               result = mid
               start = mid + 1
          else:
               end = mid - 1

     return result
               
    

print(f"{binarySearch(1, maxPos)}")