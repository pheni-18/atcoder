# https://atcoder.jp/contests/abc145/tasks/abc145_c

# 順列全探索


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    from itertools import permutations
    from math import factorial, sqrt

    n = inp()[0]
    xyl = []
    for _ in range(n):
        xy = inp()
        xyl.append(xy)

    tot = 0
    for t in permutations(xyl):
        dist = 0
        for i in range(len(t)):
            if i == 0:
                continue

            x_diff = t[i - 1][0] - t[i][0]
            y_diff = t[i - 1][1] - t[i][1]
            dist += sqrt((x_diff ** 2) + (y_diff ** 2))

        tot += dist

    ans = tot / factorial(n)
    print(ans)

if __name__ == '__main__':
    main()
