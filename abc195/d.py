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

n, m, q = sl2il(input().split())
row = n + 1 + q
inp = [input() for _ in range(row)]

wvl = []
for s in inp[:n]:
    l = s.split()
    wvl.append([int(l[0]), int(l[1])])

wvl = sorted(wvl, key=lambda x: x[1], reverse=True)

for wv in wvl:


xl = sl2il(inp[n].split())

ql = []
for s in inp[n+1:]:
    l = s.split()
    ql.append([int(l[0]), int(l[1])])

print(wvl, xl, ql)

ans_l = []
ml = [0 for _ in range(m)]


# None to 0
# print(sum(ml))
