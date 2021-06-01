row = 1
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""
l = sl2il(inp[0].split())
n, x = l
a, b, c = [-1, -1, -1]
end = False
x = x / 1000

for i in reversed(range(n + 1)):
    for j in reversed(range(n + 1)):
        k = n - i - j
        if k < 0:
            continue
        if 10*i + 5*j + k == x:
            a = i
            b = j
            c = k
            end = True
            break
    if end:
        break

print(a, b, c)



