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

n, l = sl2il(inp[0].split())

ls = []
for i in range(1, n + 1):
    ls.append(l + i - 1)

ans = 0
if 0 not in ls:
    if ls[-1] > 0:
        ls.pop(0)
    else:
        ls.pop(-1)

ans = sum(ls)
print(ans)
