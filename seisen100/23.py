# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

# 二分探索


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    from bisect import bisect_left

    n, m = inp()
    pl = [0]
    for _ in range(n):
        p = inp()[0]
        pl.append(p)

    ql = set()
    for i in range(n + 1):
        for j in range(n + 1):
            q = pl[i] + pl[j]
            if q <= m:
                ql.add(q)

    ql = list(ql)
    ql = sorted(ql)

    ans = 0
    for i in range(len(ql)):
        q1 = ql[i]
        j = max(0, bisect_left(ql, m - q1) - 1)
        q2 = ql[j]
        ans = max(ans, q1 + q2)

    print(ans)


if __name__ == '__main__':
    main()
