# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja

# ナップサックDP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, m = inp()
    cl = inp()

    dp = [n + 1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i + cl[j] <= n:
                dp[i + cl[j]] = min(dp[i + cl[j]], dp[i] + 1)

    print(dp[n])


if __name__ == '__main__':
    main()
