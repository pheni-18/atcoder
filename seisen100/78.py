# https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho1

# 累積和

# TODO: fix TLE (use numpy?) 


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
    M, N = inp()
    K = inp_one()
    map_ = []
    for _ in range(M):
        l = list(inp_one(False))
        map_.append(l)

    abcdl = [inp() for _ in range(K)]

    total = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            v = map_[i - 1][j - 1]
            cur = ['J', 'O', 'I'].index(v)
            l1 = [0, 0, 0]
            l1[cur] = 1
            for k in range(3):
                total[i][j][k] = l1[k] + total[i - 1][j][k] + total[i][j - 1][k] - total[i - 1][j - 1][k]

    for a, b, c, d in abcdl:
        ans = [0, 0, 0]
        for i in range(3):
            ans[i] = total[c][d][i] - total[a - 1][d][i] - total[c][b - 1][i] + total[a - 1][b - 1][i]

        print(f'{ans[0]} {ans[1]} {ans[2]}')


if __name__ == '__main__':
    main()
