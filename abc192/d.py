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

def f1(x, n):
    out = 0
    for i in range(1, len(str(x)) + 1):
        out += int(x[-i]) * (n**(i - 1))
    return out

x = inp[0]
m = int(inp[1])

l = sorted(x)
n = int(l[-1])
cnt = 0
end = False
while True:
    n = n + 10
    rs = f1(x, n)
    r = int(rs)
    if r > m:
        n = n - 10
        for i in range(10):
            n = n + 1
            rs = f1(x, n)
            r = int(rs)
            if r > m:
                break
            cnt = cnt + 1
        break
    cnt = cnt + 10


print(cnt)