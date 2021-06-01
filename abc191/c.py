h, w = input().split()
h = int(h)
w = int(w)
# row = 2
inp = [input() for _ in range(h)]

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
m = []
for s in inp:
    m.append(list(s))

ans = 0
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        if m[i][j] == "#":
            cnt += 1
        if m[i][j+1] == "#":
            cnt += 1
        if m[i+1][j] == "#":
            cnt += 1
        if m[i+1][j+1] == "#":
            cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
