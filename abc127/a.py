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

a, b = sl2il(inp[0].split())

if a <= 5:
    print(0)
elif 6 <= a <= 12:
    print(b // 2)
else:
    print(b)
