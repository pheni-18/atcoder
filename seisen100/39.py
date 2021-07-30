# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d

# DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    al = inp()

    dp = [[0] * 21 for _ in range(n - 1)]
    dp[0][al[0]] = 1
    for i in range(n - 2):
        for j in range(21):
            if dp[i][j] <= 0:
                continue

            a = al[i + 1]
            if 0 <= (j + a) <= 20:
                dp[i + 1][j + a] += dp[i][j]
            if 0 <= (j - a) <= 20:
                dp[i + 1][j - a] += dp[i][j]

    print(dp[n - 2][al[-1]])


if __name__ == '__main__':
    main()
