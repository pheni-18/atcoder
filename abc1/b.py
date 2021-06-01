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

m = int(inp[0])

vv = -1
if m < 100:
    vv = 0
elif 100 <= m <= 5000:
    vv = m / 1000 * 10
elif 6000 <= m <= 30000:
    vv = m / 1000 + 50
elif 35000 <= m <= 70000:
    vv = (((m / 1000) - 30) / 5) + 80
elif 70000 < m:
    vv = 89

vv = str(int(vv)).zfill(2)
print(vv)
