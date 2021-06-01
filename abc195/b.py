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

a, b, w = sl2il(inp[0].split())

min_ = -1
max_ = -1
wg = w * 1000
for i in range(1, wg+1):
    if a <= (wg / i) <= b:
        if min_ == -1:
            min_ = i
        max_ = i

if min_ == -1 and max_ == -1:
    print('UNSATISFIABLE')
else:
    print(min_, max_)