import sys
sys.setrecursionlimit(10**8)



stringA = input()
stringB = input()

def bottomUPLCS(strA, strB, lenA, lenB):
        table = [[0] * (lenB + 1) for _ in range(lenA + 1)]

        for i in range(1, lenA + 1):
                for j in range(1, lenB + 1):
                        if(strA[i - 1] == strB[j - 1]):
                                table[i][j] = table[i - 1][j - 1] + 1
                        elif table[i - 1][j] >= table[i][j - 1]:
                                table[i][j] = table[i - 1][j]
                        else:
                                table[i][j] = table[i][j - 1]

        return table[lenA][lenB]

result = bottomUPLCS(stringA, stringB, len(stringA), len(stringB))
print(str(result))