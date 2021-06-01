n = int(input())
# row = 2
inp = [input() for _ in range(n)]

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
wa = 0
ans = 200001
al = []
bl = []
for s in inp:
    a, b = sl2il(s.split())
    al.append(a)
    bl.append(b)

for i, a in enumerate(al):
    for j, b in enumerate(bl):
        c = a if a > b else b
        if i == j:
            c = a + b
        if c < ans:
            ans = c

print(ans)



