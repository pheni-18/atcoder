# https://atcoder.jp/contests/joi2015ho/tasks/joi2015ho_a

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
    N, M = inp()
    pl = inp()
    rails = [inp() for _ in range(N - 1)]

    map_ = [0] * N
    for i in range(M - 1):
        s = pl[i]
        e = pl[i + 1]
        if s > e:
            s, e = e, s

        map_[s] += 1
        if e <= N - 1:
            map_[e] -= 1

    for i in range(1, N):
        map_[i] += map_[i - 1]

    ans = 0
    for i in range(N - 1):
        a, b, c = rails[i]
        cnt = map_[i + 1]
        ans += min(a * cnt, b * cnt + c)

    print(ans)
        

if __name__ == '__main__':
    main()
