# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d

# DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def s2num(s):
    if s == 'R':
        return 0
    elif s == 'B':
        return 1
    elif s == 'W':
        return 2
    else:
        return 3


def main():
    n = inp()[0]
    sll = [list(inp(False)[0]) for _ in range(5)]

    color_num = 4
    dp = [[5001] * (color_num - 1) for _ in range(n)]

    for i in range(n):
        for j in range(color_num - 1):
            for k in range(color_num - 1):
                if j == k:
                    continue

                c = 0
                for sl in sll:
                    if not s2num(sl[i]) == k:
                        c += 1

                if i == 0:
                    dp[i][k] = min(dp[i][k], c)
                    continue

                dp[i][k] = min(dp[i][k], dp[i - 1][j] + c)

    print(min(dp[-1]))


if __name__ == '__main__':
    main()
