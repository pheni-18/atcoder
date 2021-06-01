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

a, b = sl2il(inp[0].split())
c, d = sl2il(inp[1].split())

print(b - c)