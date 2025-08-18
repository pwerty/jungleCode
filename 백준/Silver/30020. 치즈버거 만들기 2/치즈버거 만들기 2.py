import sys
input = sys.stdin.readline


def printAns(subTr, tempAns):
    tmpString = ""
    while(subTr != 0):
        tmpString += "ab"
        subTr -= 1
    for i in range(0, tempAns):
        print("ab" + tmpString +"a")

def main():
    patty, cheese = map(int, input().strip().split())
    subTract = 0
    cheeseTmp, pattyTmp = 0, 0
    tmpAns = 0

    if (patty <= cheese):
        print("NO")
        return

    if(patty > (cheese * 2)):
        print("NO")
        return

    while (subTract < min(patty, cheese)):
        cheeseTmp = cheese
        pattyTmp = patty
        tmpAns = 0

        if(cheeseTmp + 1 == pattyTmp):
            print("YES")
            print(tmpAns + 1)
            printAns(subTract, tmpAns)
            lastPrintContent = ""
            while(cheeseTmp != 0):
                cheeseTmp -= 1
                lastPrintContent += "ab"
            print(lastPrintContent + "a")
            return

        while(cheeseTmp + 1 < pattyTmp):
            cheeseTmp -= (1 + subTract)
            pattyTmp -= (2 + subTract)
            tmpAns += 1

            if(cheeseTmp + 1 == pattyTmp):
                print("YES")
                print(tmpAns + 1)
                printAns(subTract, tmpAns)
                lastPrintContent = ""
                while(cheeseTmp != 0):
                    cheeseTmp -= 1
                    lastPrintContent += "ab"
                print(lastPrintContent + "a")
                return
        subTract += 1

main()
