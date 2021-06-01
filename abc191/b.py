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

n, x = sl2il(inp[0].split())
a = sl2il(inp[1].split())

ad = [i for i in a if i != x]

if ad == []:
    print("")
else:
    print(" ".join(il2sl(ad)))