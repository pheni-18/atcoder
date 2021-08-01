# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d

# DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    d, n = inp()
    tl = [inp()[0] for _ in range(d)]
    cloth_l = []
    for _ in range(n):
        cloth_l.append(inp())

    dp = [[0] * n for _ in range(d)]
    for i in range(d - 1):
        for j in range(n):
            a1, b1, c1 = cloth_l[j]
            if not (a1 <= tl[i] <= b1):
                continue

            for k in range(n):
                a2, b2, c2 = cloth_l[k]
                if not (a2 <= tl[i + 1] <= b2):
                    continue

                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + abs(c1 - c2))

    print(max(dp[-1]))


if __name__ == '__main__':
    main()
