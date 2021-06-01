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
    n = inp()[0]
    p = inp()
    sp = sorted(p)

    cnt = 0
    for i in range(n):
        if not p[i] == sp[i]:
            cnt += 1

    if cnt <= 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
