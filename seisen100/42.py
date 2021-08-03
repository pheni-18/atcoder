# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d

# DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, m = inp()
    dl = [inp()[0] for _ in range(n)]
    cl = [inp()[0] for _ in range(m)]

    dp = [[1001001001] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        dp[i][0] = 0

    for i in range(m):
        for j in range(1, n + 1):
            f = dl[j - 1] * cl[i]
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - 1] + f, dp[i][j])

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
