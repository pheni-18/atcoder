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

import math


def lcm(c, d):
    return c * d // math.gcd(c, d)


def f(x, c, d):
    r = x
    r -= x // c
    r -= x // d
    r += x // lcm(c, d)
    return r


a, b, c, d = sl2il(inp[0].split())

ans = f(b, c, d) - f(a - 1, c, d)

print(ans)
