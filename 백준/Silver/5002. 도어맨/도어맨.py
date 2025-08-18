import sys
input = sys.stdin.readline


def main():
    doorManMem = int(input())
    waitLine = list(map(str, input().rstrip()))
    man, woman = 0, 0
    ans = 0
    for i in range(len(waitLine)):
        if abs(man - woman) < doorManMem:
            if waitLine[i] == 'M':
                man += 1
            else:
                woman += 1
            ans += 1
        else:
            if waitLine[i] == 'M':
                if abs(man + 1 - woman) < doorManMem:
                    man += 1
                    ans += 1
                else:
                    if i + 1 < len(waitLine) and waitLine[i + 1] == 'W':
                        waitLine[i], waitLine[i + 1] = waitLine[i + 1], waitLine[i]
                        woman += 1
                        ans += 1
                    else:
                        break
            else:
                if abs(woman + 1 - man) < doorManMem:
                    woman += 1
                    ans += 1
                else:
                    if i + 1 < len(waitLine) and waitLine[i + 1] == 'M':
                        waitLine[i], waitLine[i + 1] = waitLine[i + 1], waitLine[i]
                        man += 1
                        ans += 1
                    else:
                        break
    print(ans)

main()