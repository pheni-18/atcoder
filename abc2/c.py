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

"""

from decimal import Decimal
n , k = sl2il(inp[0].split())

l = []
for i in range(1, n + 1):
    th = -1
    w = 1
    for j in range(0, 30):
        if k <= (i * w):
            th = j
            break
        w *= 2

    l.append(Decimal((1/n) * ((1/2) ** th)))

print(sum(l))