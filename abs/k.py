n = int(input())
# row = 2
inp = [input() for _ in range(n)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""

l = inp
t1 = 0
x1, y1 = (0, 0)
ans = "No"

for s in l:
    t2, x2, y2 = sl2il(s.split())
    if abs(t2 - t1) < abs(x2 - x1) + abs(y2 - y1):
        break
    if (t2 - t1) % 2 != ((x2 - x1) + (y2 - y1)) % 2:
        break
    t1 = t2
    x1 = x2
    y1 = y2
else:
    ans = "Yes"

print(ans)
