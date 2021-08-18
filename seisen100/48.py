# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp

# DP

# TODO: fix TLE


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    nl = []
    wll = []
    while True:
        n = inp()[0]
        if n == 0:
            break

        nl.append(n)
        wll.append(inp())

    for n, wl in zip(nl, wll):
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n + 1):
            for l in range(n):
                r = l + d - 1
                if r > n - 1:
                    continue

                if dp[l + 1][r - 1] == d - 2:
                    if abs(wl[l] - wl[r]) <= 1:
                        dp[l][r] = d

                for k in range(l, r):
                    dp[l][r] = max(dp[l][r], dp[l][k] + dp[k + 1][r])

        print(dp[0][-1])


if __name__ == '__main__':
    main()
