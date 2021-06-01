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

s = inp[0]

a = s[:2]
b = s[2:]

ai = int(a)
bi = int(b)

ap = ''
if ai == 0:
    ap = 'Y'
elif ai <= 12:
    ap = 'YM'
elif ai <= 99:
    ap = 'Y'

bp = ''
if bi == 0:
    bp = 'Y'
elif bi <= 12:
    bp = 'YM'
elif bi <= 99:
    bp = 'Y'

if ap == 'YM' and bp == 'YM':
    print('AMBIGUOUS')
elif ap == 'YM' and bp == 'Y':
    print('MMYY')
elif ap == 'Y' and bp == 'YM':
    print('YYMM')
else:
    print('NA')