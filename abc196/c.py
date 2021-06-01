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

n = int(inp[0])
ans = 0


for i in range(1, 1000000):
    s = str(i)
    x = int(s + s)
    if x <= n:
        ans += 1

print(ans)
