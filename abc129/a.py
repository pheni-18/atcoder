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
p, q, r = sl2il(inp[0].split())

t1 = p + q
t2 = q + r
t3 = p + r

l = [t1, t2, t3]

print(min(l))
