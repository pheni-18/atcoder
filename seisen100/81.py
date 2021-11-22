# https://atcoder.jp/contests/abc014/tasks/abc014_3

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
    n = inp_one()
    abl = [inp() for _ in range(n)]

    M = 10 ** 6 + 1
    map_ = [0] * M
    for a, b in abl:
        map_[a] += 1
        if b + 1 < M:
            map_[b + 1] -= 1

    for i in range(1, M):
        map_[i] += map_[i - 1]

    print(max(map_))


if __name__ == '__main__':
    main()
