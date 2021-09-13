# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_d

# bitDP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    sl = list(inp(False)[0])
    d = {'J': 1, 'O': 2, 'I': 4}
    sche = [0] * (n + 1)
    for i in range(n):
        s = sl[i]
        sche[i + 1] = d[s]

    dp = [[0] * (n + 1) for _ in range(2 ** 3)]
    dp[1][0] = 1

    for i in range(n):
        for now in range(2 ** 3):
            for next in range(2 ** 3):
                if not now & next:
                    continue

                if not next & sche[i + 1]:
                    continue

                dp[next][i + 1] += dp[now][i]
                dp[next][i + 1] %= 10007

    ans = 0
    for i in range(2 ** 3):
        ans += dp[i][n]

    print(ans % 10007)


if __name__ == '__main__':
    main()
