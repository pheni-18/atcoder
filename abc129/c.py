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

n, m = sl2il(inp[0].split())

broken = -1
broken_cnt = 0
if broken_cnt < m:
    broken = int(input())
    broken_cnt += 1

mod = 1000000007
dp = [1]
for i in range(1, n + 1):
    if i == broken:
        dp.append(0)
        if broken_cnt < m:
            broken = int(input())
            broken_cnt += 1
        continue

    if i == 1:
        dp.append(dp[i-1])
    else:
        dp.append((dp[i-1] + dp[i-2]) % mod)


print(dp[n])
