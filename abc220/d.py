def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    al = inp()

    dp = [[0] * 10 for _ in range(n)]
    dp[0][al[0]] = 1
    for i in range(1, n):
        for j in range(10):
            # f
            nxt = (j + al[i]) % 10
            dp[i][nxt] += dp[i - 1][j]

            # g
            nxt = (j * al[i]) % 10
            dp[i][nxt] += dp[i - 1][j]

            dp[i][nxt] %= 998244353

    for i in range(10):
        ans = dp[n - 1][i] % 998244353
        print(ans)


if __name__ == '__main__':
    main()
