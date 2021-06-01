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

ans = set()
end = False
for a in range(2, n):
    for b in range(2, n):
        x = a ** b
        if x <= n:
            ans.add(x)
        else:
            if b == 2:
                end = True
            break
    if end:
        break

print(n - len(ans))
