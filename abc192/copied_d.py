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
sl2il(inp[].split())
"""

x = inp[0]
m = int(inp[1])

l = sorted(x)
n = int(l[-1])
cnt = 0
while True:
    n = n + 1
    rs = int(x, n)
    r = int(rs)
    if r > m:
        break
    cnt = cnt + 1

print(cnt)