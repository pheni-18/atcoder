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
import math

r, x, y = sl2il(inp[0].split())

z = math.sqrt(x ** 2 + y ** 2)
ans = -1
if z < r:
    ans = 2
elif z % r == 0:
    ans = z / r
else:
    ans = (z // r) + 1

print(int(ans))