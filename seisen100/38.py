# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja

# ナップサックDP

# TODO: fix TLE


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    q = inp()[0]
    xy_l = []
    for _ in range(q):
        x = inp(False)[0]
        y = inp(False)[0]
        xy_l.append((list(x), list(y)))

    for xy in xy_l:
        x, y = xy
        x_len, y_len = len(x), len(y)
        dp = [[0] * (y_len + 1) for _ in range(x_len + 1)]
        for i in range(x_len):
            for j in range(y_len):
                if x[i] == y[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        print(dp[x_len][y_len])


if __name__ == '__main__':
    main()
