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

a, b, c = sl2il(inp[0].split())

if a ** 2 + b ** 2 < c **2:
    print('Yes')
else:
    print('No')