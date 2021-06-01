h, w, x, y = input().split()
h = int(h)
w = int(w)
x = int(x)
y = int(y)
row = h
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

def il2sl(l):
    return list(map(lambda x: str(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""

l = []
for i in range(h):
    l.append(list(inp[i]))

ans = 1
for i in reversed(range(0, y)):
    if i == y-1:
        continue
    if l[x-1][i] == '.':
        ans += 1
    else:
        break

for i in range(y-1, w):
    if i == y-1:
        continue
    if l[x-1][i] == '.':
        ans += 1
    else:
        break

for i in reversed(range(0, x)):
    if i == x-1:
        continue
    if l[i][y-1] == '.':
        ans += 1
    else:
        break

for i in range(x-1, h):
    if i == x-1:
        continue
    if l[i][y-1] == '.':
        ans += 1
    else:
        break

print(ans)