# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja

# ワーシャルフロイド法


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
    V, E = inp()
    stdl = [inp() for _ in range(E)]

    dp = [[float('inf')] * V for _ in range(V)]

    for s, t, d in stdl:
        dp[s][t] = d

    for v in range(V):
        dp[v][v] = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    exist_negative_cycle = False
    for v in range(V):
        if dp[v][v] < 0:
            exist_negative_cycle = True

    if exist_negative_cycle:
        print('NEGATIVE CYCLE')
        return

    ansll = [[''] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if dp[i][j] == float('inf'):
                ansll[i][j] = 'INF'
            else:
                ansll[i][j] = str(dp[i][j])

    for ansl in ansll:
        print(' '.join(ansl))


if __name__ == '__main__':
    main()
