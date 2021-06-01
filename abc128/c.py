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

n, m = sl2il(inp[0].split())

l = [input() for _ in range(m)]

pl = sl2il(input().split())

# swl = [0 for _ in range(n)]
ans = 0
for i in range(2 ** n):
    s2 = bin(i)
    s2_ = s2[2:]
    swl_ = list(s2_.zfill(n))
    swl = sl2il(swl_)

    ok = True
    for j, ks in enumerate(l):
        ksl = ks.split()
        k = int(ksl[0])
        sl_ = ksl[1:]
        sl = sl2il(sl_)

        kosuu = 0
        for s in sl:
            if swl[s-1] == 1:
                kosuu += 1

        if kosuu % 2 != pl[j]:
            ok = False
    if ok:
        ans += 1

print(ans)
