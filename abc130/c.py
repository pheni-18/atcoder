# n = int(input())
row = 1
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

w, h, x, y = sl2il(inp[0].split())

c = [w/2, h/2]

ans1 = w * h / 2
ans2 = -1
if x == c[0] and y == c[1]:
    ans2 = 1
else:
    ans2 = 0
print(ans1, ans2)
