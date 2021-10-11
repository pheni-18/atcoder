# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=ja

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
    al = [inp_one() for _ in range(n)]

    dp = [al[0]]
    for a in al:
        if a > dp[-1]:
            dp.append(a)
        else:
            cur = bisect_left(dp, a)
            dp[cur] = a

    print(len(dp))


if __name__ == '__main__':
    main()
