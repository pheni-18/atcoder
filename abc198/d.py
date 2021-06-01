# n = int(input())
row = 3
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

s1 = inp[0]
s2 = inp[1]
s3 = inp[2]
# s1: send, s2: more, s3: money

cs = set()
sl1 = list(s1)
sl2 = list(s2)
sl3 = list(s3)

ans = 'UNSOLVABLE'
for s in sl1:
    cs.add(s)
for s in sl2:
    cs.add(s)
for s in sl3:
    cs.add(s)

def f1(sl, cl):
    nums = []
    for s in sl:
        ind = cl.index(s)
        nums.append(str(l[ind]))
    ss = ''.join(nums)
    return int(ss)

l = [-1 for _ in range(len(cs))]
kouho = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def dfs(i, kouho):
    if i == len(cs):
        cl = list(cs)
        n1 = f1(sl1, cl)
        n2 = f1(sl2, cl)
        n3 = f1(sl3, cl)
        if n1 + n2 == n3:
            global ans
            ans = [n1, n2, n3]
        return

    for k in kouho:
        l[i] = k
        kouho2 = list(kouho)
        print(kouho2, k)
        ind = kouho2.index(k)
        kouho2.pop(ind)
        dfs(i + 1, kouho2)


if len(cs) <= 10:
    i = 0
    dfs(i, kouho)

if ans == 'UNSOLVABLE':
    print(ans)
else:
    for sss in ans:
        print(sss)