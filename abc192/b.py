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

s = inp[0]
o = []
e = []
for i, a in enumerate(s):
    if i % 2 == 0:
        o.append(a)
    else:
        e.append(a)

oo = "".join(o)
ee = "".join(e)

if oo.islower() and (ee.isupper() or ee == ""):
    print("Yes")
else:
    print("No")