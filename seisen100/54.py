# https://atcoder.jp/contests/abc006/tasks/abc006_4

# DP Others


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inp_one(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    s = input()
    return int(s) if to_int else s


def main():
    from bisect import bisect_left
    n = inp_one()
    cl = [inp_one() for _ in range(n)]

    dp = [cl[0]]
    for c in cl:
        if c > dp[-1]:
            dp.append(c)
        else:
            cur = bisect_left(dp, c)
            dp[cur] = c

    print(n - len(dp))


if __name__ == '__main__':
    main()
