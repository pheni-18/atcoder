# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_b

# 区間DP


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    al = [inp()[0] for _ in range(n)]
    al = al + al

    dp = [[0] * (n * 2) for _ in range(n * 2)]
    for d in range(n):
        for l in range(n * 2):
            r = l + d

            if r >= n * 2:
                break

            if d == 0:
                dp[l][r] = al[l]
            elif d == 1:
                dp[l][r] = max(al[l], al[r])
            else:
                vl = al[l]
                if al[r] > al[l + 1]:
                    vl += dp[l + 1][r - 1]
                else:
                    vl += dp[l + 2][r]

                vr = al[r]
                if al[l] > al[r - 1]:
                    vr += dp[l + 1][r - 1]
                else:
                    vr += dp[l][r - 2]

                dp[l][r] = max(vl, vr)

    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][i + n - 1])

    print(ans)


if __name__ == '__main__':
    main()
