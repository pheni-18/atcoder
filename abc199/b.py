# n = int(input())
row = 3
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
al = sl2il(inp[1].split())
bl = sl2il(inp[2].split())

ans = 0
for i in range(1, 1001):
    cnt = 0
    for j in range(n):
        if al[j] <= i <= bl[j]:
            cnt += 1
    if cnt == n:
        ans += 1

print(ans)

