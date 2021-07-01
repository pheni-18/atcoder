# https://atcoder.jp/contests/abc150/tasks/abc150_c

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

    n = inp()[0]
    pl = inp(False)
    ql = inp(False)

    nl = [str(i + 1) for i in range(n)]

    cnt = 0
    a = 0
    b = 0
    for t in permutations(nl):
        cnt += 1
        if pl == list(t):
            a = cnt

        if ql == list(t):
            b = cnt

    print(abs(a - b))


if __name__ == '__main__':
    main()
