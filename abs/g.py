row = 2
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""

a = int(inp[0])
l = sl2il(inp[1].split())

alice = []
bob = []

for i in range(a):
    if i % 2 == 0:
        alice.append(max(l))
    else:
        bob.append(max(l))
    l.remove(max(l))
print(sum(alice) - sum(bob))