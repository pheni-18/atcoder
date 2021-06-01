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
sl = list(s)

ans = 'Good'
for i in range(3):
    if sl[i] == sl[i+1]:
        ans = 'Bad'

print(ans)