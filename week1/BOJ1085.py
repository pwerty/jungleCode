x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

result = min(w - x, abs(0 - x), h - y, abs(0 - y))

print(result)