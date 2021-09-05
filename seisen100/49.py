# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja

# bitDP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    v, e = inp()
    stdl = [inp() for _ in range(e)]
    g = [[float('inf')] * v for _ in range(v)]
    for s, t, d in stdl:
        g[s][t] = d

    dp = [[float('inf')] * v for _ in range(2 ** v)]
    dp[0][0] = 0

    for s in range(2 ** v):
        for l in range(v):
            for u in range(v):
                if not (s >> u) & 1 and s != 0:
                    continue
                if (s >> l) & 1:
                    continue
                if dp[s][u] + g[u][l] < dp[s | (1 << l)][l]:
                    dp[s | (1 << l)][l] = dp[s][u] + g[u][l]

    if dp[2 ** v - 1][0] != float('inf'):
        print(dp[2 ** v - 1][0])
    else:
        print(-1)


if __name__ == '__main__':
    main()
