n = int(input())

row = 1
inp = [input() for _ in range(n)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""

l = sl2il(inp)

l = set(l)
print(len(l))