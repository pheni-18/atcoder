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

sl2il(inp[].split())
"""

f, k = sl2il(inp[0].split())
g1 = 0
g2 = 0
for i in range(k):
    fs = str(f)
    g1l = sorted(fs)
    g1l.reverse()
    g1 = int("".join(g1l))

    g2l = sorted(fs)
    g2 = int("".join(g2l))

    f = g1 - g2
    if f == 0:
        break
print(f)


