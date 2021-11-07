# https://atcoder.jp/contests/abc012/tasks/abc012_4

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
    N, M = inp()
    abtl = [inp() for _ in range(M)]

    dp = [[float('inf')] * N for _ in range(N)]

    for a, b, t in abtl:
        a -= 1
        b -= 1
        dp[a][b] = t
        dp[b][a] = t

    for v in range(N):
        dp[v][v] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    ans = float('inf')
    for i in range(N):
        mt = max(dp[i])
        ans = min(ans, mt)

    print(ans)


if __name__ == '__main__':
    main()
