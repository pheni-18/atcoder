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

keta = len(str(n))
ans = 0

if 6 >= keta >= 4:
    ans += n - 999
elif 9 >= keta >= 7:
    ans += 999000
    ans += (n - 999999) * 2
elif 12 >= keta >= 10:
    ans += 999000
    ans += 999000000 * 2
    ans += (n - 999999999) * 3
elif 15 >= keta >= 13:
    ans += 999000
    ans += 999000000 * 2
    ans += 999000000000 * 3
    ans += (n - 999999999999) * 4
elif keta == 16:
    ans += 999000
    ans += 999000000 * 2
    ans += 999000000000 * 3
    ans += 999000000000000 * 4
    ans += 5

print(ans)