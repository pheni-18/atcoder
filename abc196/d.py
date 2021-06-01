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

h, w, a, b = sl2il(inp[0].split())
hw = h * w

ans = {}
l = [[0 for _ in range(w)] for _ in range(h)]
nokori = [a, b]
for i in range(a + b):
    mode = ''
    if nokori[0] > 0:
        nokori[0] -= 1
        mode = 'a'
    elif nokori[1] > 0:
        nokori[1] -= 1
        mode = 'b'
    else:
        break

    if mode == 'a':


print(len(ans))

