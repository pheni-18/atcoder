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

k = int(inp[0])
s = list(inp[1])
_ = s.pop()
s = sl2il(s)
t = list(inp[2])
_ = t.pop()
t = sl2il(t)

if k >= 10:
    k = 10

zan = [k, k, k, k, k, k, k, k, k]
for i in s:
    zan[i - 1] = zan[i - 1] - 1
for i in t:
    zan[i - 1] = zan[i - 1] - 1

won_s = 0
total = 0
for i in range(1, 10):
    for j in range(1, 10):
        if zan[i - 1] == 0 or zan[j - 1] == 0:
            continue
        if i == j and zan[i - 1] == 1:
            continue
        sl = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        s.append(i)
        for k in s:
            sl[k - 1] = sl[k - 1] + 1
        print("sl", sl)
        s.pop()
        s_score = 0
        for ii, jj in enumerate(sl):
            print(ii, jj)
            print((ii + 1) * (10 ** jj))
            s_score = s_score + (ii + 1) * (10 ** jj)

        tl = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        t.append(j)
        for k in t:
            tl[k - 1] = tl[k - 1] + 1
        print("tl", tl)
        t.pop()
        t_score = 0
        for ii, jj in enumerate(tl):
            print(ii, jj)
            print((ii + 1) * (10 ** jj))
            t_score = t_score + (ii + 1) * (10 ** jj)

        print(s_score, t_score)
        total = total + 1
        if s_score > t_score:
            won_s = won_s + 1
print(won_s, total)
print(won_s / total)
