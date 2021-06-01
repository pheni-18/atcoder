# n = int(input())
row = 2
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

def il2sl(l):
    return list(map(lambda x: str(x), l))

"""
inp[]

inp[].split()
sl2il(inp[].split())
"""

n = int(inp[0])
l = sl2il(inp[1].split())

sal = []
for i in range(n):
    wl1 = l[:i + 1]
    wl2 = l[i + 1:]

    sum1 = sum(wl1)
    sum2 = sum(wl2)

    sal.append(abs(sum1 - sum2))

print(min(sal))
