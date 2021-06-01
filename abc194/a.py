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
c = a + b
ans = -1
if c >= 15 and b >= 8:
    ans = 1
elif c >= 10 and b >= 3:
    ans = 2
elif c >= 3:
    ans = 3
else:
    ans = 4
print(ans)
