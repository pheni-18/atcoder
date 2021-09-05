def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    N, M = inp()
    stdtimel = [inp() for _ in range(M)]
    path = [[(float('inf'), 0)] * N for _ in range(N)]
    for s, t, d, time in stdtimel:
        s -= 1
        t -= 1
        tpl = (d, time)
        path[s][t] = tpl
        path[t][s] = tpl

    dp = [[[float('inf'), 0]] * N for _ in range(2 ** N)]
    dp[0][0] = [0, 1]

    for s in range(2 ** N):
        for u in range(N):
            if not (s >> u) & 1 and s != 0:
                continue

            for v in range(N):
                if (s >> v) & 1:
                    continue

                d, time = path[u][v]
                if dp[s][u][0] + d > time:
                    continue

                if dp[s][u][0] + d < dp[s | (1 << v)][v][0]:
                    dp[s | (1 << v)][v] = [dp[s][u][0] + d, dp[s][u][1]]
                elif dp[s][u][0] + d == dp[s | (1 << v)][v][0]:
                    dp[s | (1 << v)][v][1] += dp[s][u][1]

    ansl = dp[2 ** N - 1][0]
    if ansl[0] == float('inf'):
        print('IMPOSSIBLE')
    else:
        print(ansl[0], ansl[1])


if __name__ == '__main__':
    main()
