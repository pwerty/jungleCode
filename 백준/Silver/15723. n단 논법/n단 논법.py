import sys
input = sys.stdin.readline
graph = {}

def add_relation(x, y):
    graph.setdefault(x, []).append(y)

def has_path(start, end):
    visited = set()
    stack = [start]
    while stack:
        cur = stack.pop()
        if cur == end:
            return True
        if cur in visited:
            continue
        visited.add(cur)
        for nxt in graph.get(cur, []):
            stack.append(nxt)
    return False

# 예시
preProcessCnt = int(input())
for i in range(0, preProcessCnt):
    s = input()
    x, _, y = s.split()  # ["a", "is", "b"]
    add_relation(x, y)

postProcessCnt = int(input())
for i in range(0, postProcessCnt):
    s = input()
    x, _, y = s.split()  # ["a", "is", "b"]
    if(has_path(x, y)):
        print("T")
    else:
        print("F")
