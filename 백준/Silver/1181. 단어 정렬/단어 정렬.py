caseInput = int(input())
wordList = []
for i in range(caseInput):
    wordList.append(input())

uniqueList = []
afterWordList = sorted(wordList, key=lambda x: (len(x), x))

for item in afterWordList:
    if item not in uniqueList:
        uniqueList.append(item)

for i in range(len(uniqueList)):
    print(uniqueList[i])