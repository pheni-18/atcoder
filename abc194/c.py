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

n = int(inp[0])
al = sl2il(inp[1].split())

x = len(al) - 1
total = 0
wa = sum(al)

for i in al:
    total += x * (i ** 2)
    wa -= i
    total -= 2 * i * wa

print(total)
