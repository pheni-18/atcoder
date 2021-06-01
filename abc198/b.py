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

def is_pali(l):
    h = len(l) // 2
    for i in range(h):
        if l[i] != l[(-1 * i) - 1]:
            return False
    return True

n = int(inp[0])
sn = str(n)
l = list(sn)
ans = 'No'

for _ in range(11):
    if is_pali(l):
        ans = 'Yes'
    l.insert(0, '0')

print(ans)