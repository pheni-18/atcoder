# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d

# DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, k = inp()
    ad = {}
    for _ in range(k):
        a, b = inp()
        ad[a] = b
    dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(4):
            for k in range(4):
                a = ad.get(i, None)
                for p in range(1, 4):
                    if a is not None:
                        if not a == p:
                            continue
                    if j == k == p:
                        continue

                    dp[i][p][j] += dp[i - 1][j][k] % 10000

    tot = 0
    for j in range(4):
        for k in range(4):
            tot += dp[-1][j][k]
            tot %= 10000

    print(tot)


if __name__ == '__main__':
    main()
