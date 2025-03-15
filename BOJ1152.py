inputSentence = input()

result = inputSentence.count(" ") + 1

if inputSentence.startswith(" "):
    result -= 1

if inputSentence.endswith(" "):
    result -= 1

print(result)