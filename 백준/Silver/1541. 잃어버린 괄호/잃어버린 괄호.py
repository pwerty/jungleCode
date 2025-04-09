import sys
input = sys.stdin.readline

targetSentence = input()
isMinus = False
num = ""
result = 0
for i in range(len(targetSentence)):
    if(targetSentence[i] == '-' or targetSentence[i] == '+' or i == len(targetSentence) - 1):
        if(isMinus):
            result -= int(num)
            num = ""
        else:
            result += int(num)
            num = ""
    else:
        num += targetSentence[i]
    
    if(targetSentence[i] == '-'):
        isMinus = True

print(result)