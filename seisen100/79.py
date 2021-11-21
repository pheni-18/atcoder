# https://atcoder.jp/contests/abc106/tasks/abc106_d

# 累積和


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
    N, M, Q = inp()
    lrl = [inp() for _ in range(M)]
    pql = [inp() for _ in range(Q)]

    map_ = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in lrl:
        map_[l][r] += 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            map_[i][j] += map_[i - 1][j] + map_[i][j - 1] - map_[i - 1][j - 1]
    
    for p, q in pql:
        ans = map_[q][q] - map_[p - 1][q] - map_[q][p - 1] + map_[p - 1][p - 1]
        print(ans)


if __name__ == '__main__':
    main()
