# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=ja

# 区間DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    pl = inp()
    for _ in range(n - 1):
        r, c = inp()
        pl.append(c)

    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for d in range(1, n):
        for r in range(n - d):
            c = r + d
            for k in range(d):
                p = (pl[r]*pl[r + k + 1] * pl[c + 1])
                v = dp[r][r + k] + dp[r + k + 1][c] + p
                dp[r][c] = min(dp[r][c], v)

    print(dp[0][-1])


if __name__ == '__main__':
    main()
