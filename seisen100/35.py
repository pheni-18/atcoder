# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja

# ナップサックDP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, w_lim = inp()
    vl = []
    wl = []
    for _ in range(n):
        v, w = inp()
        vl.append(v)
        wl.append(w)

    dp = [[0] * (w_lim + 1) for _ in range(n + 1)]
    for i in range(n):
        for w in range(w_lim + 1):
            if w - wl[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - wl[i]] + vl[i])

            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

    print(dp[n][w_lim])


if __name__ == '__main__':
    main()
