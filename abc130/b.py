# n = int(input())
row = 2
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

def il2sl(l):
    return list(map(lambda x: str(x), l))

"""
inp[]
int(inp[])
inp[].split()

"""

n, x = sl2il(inp[0].split())

ll = sl2il(inp[1].split())

a = 0
ans = 1
for l in ll:
    a += l
    if a <= x:
        ans += 1

print(ans)

