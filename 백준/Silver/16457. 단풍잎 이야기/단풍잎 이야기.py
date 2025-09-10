import sys
input = sys.stdin.readline

isSelected = [False] * 21
mySkillBar = set()
questList = []
ans = 0


# 기본 입력 받아오기
maxSkillSelection, questCnt, questReqSkill = map(int, input().split())
for i in range(questCnt):
    quest = list(map(int, input().split()))
    questList.append(quest)


# N과 M 식 백트레킹 작성
def SkillSelection(depth, startPivot):
    global ans

    # n개 선택한 경우에 대한 선택지
    if(depth == maxSkillSelection):
        tmpAns = 0
        for quest in questList:
            tmpSet = set(quest)
            if(tmpSet.issubset(mySkillBar)):
                tmpAns += 1
        ans = max(ans, tmpAns)
        return

    for i in range(startPivot, maxSkillSelection*2 + 1): # startPivot Must starts with 1!!!! not 0!!!!!
        isSelected[i] = True
        mySkillBar.add(i)
        SkillSelection(depth + 1, i + 1)
        isSelected[i] = False
        mySkillBar.remove(i)

for a in range(1, maxSkillSelection*2):
    SkillSelection(0, a)

print(ans)




