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

n = int(inp[0])

l = []
for i in range(n):
    s, p = input().split()
    p = int(p)

    ss = [x['s'] for x in l]

    for d in l:
        if s == d['s']:
            d['cl'].append({
                'idx': i + 1,
                'p': p,
            })
            break
    else:
        l.append({
            's': s,
            'cl': [{
                'idx': i + 1,
                'p': p,
            }],
        })

sorted_l = sorted(l, key=lambda x: x['s'])

for d in sorted_l:
    sorted_cl = sorted(d['cl'], key=lambda x: x['p'], reverse=True)
    d['sorted_cl'] = sorted_cl

for d in sorted_l:
    for cl in d['sorted_cl']:
        print(cl['idx'])
