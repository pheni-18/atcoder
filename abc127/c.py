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

n, m = sl2il(inp[0].split())

min_ = 0
max_ = 100001

ans = -1

for i in range(m):
    l = input()
    l, r = sl2il(l.split())
    if l > min_:
        min_ = l

    if r < max_:
        max_ = r

ans = max_ - min_ + 1

if min_ > max_:
    ans = 0
print(ans)
