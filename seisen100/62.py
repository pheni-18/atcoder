# https://atcoder.jp/contests/abc079/tasks/abc079_d

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
    H, W = inp()
    N = 10
    cll = [inp() for _ in range(N)]
    all = [inp() for _ in range(H)]

    cntl = [0] * N
    for i in range(H):
        for j in range(W):
            a = all[i][j]
            if a != -1:
                cntl[a] += 1

    dp = cll
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    ans = 0
    for i in range(N):
        ans += dp[i][1] * cntl[i]

    print(ans)


if __name__ == '__main__':
    main()
