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

l = [sl2il(x.split()) for x in inp]

ans = -1
ans_l = []
for a in l:
    if a[2] - a[0] >= 1:
        ans_l.append(a[1])
if not ans_l == []:
    ans = min(ans_l)
print(ans)


