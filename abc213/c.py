def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from bisect import bisect_left
    h, w, n = inp()
    pl = []
    yl = set()
    xl = set()
    for i in range(n):
        a, b = inp()
        pl.append((a, b))
        yl.add(a)
        xl.add(b)

    xl = sorted(list(xl))
    yl = sorted(list(yl))
    for i in range(n):
        a, b = pl[i]

        a2 = bisect_left(yl, a) + 1
        b2 = bisect_left(xl, b) + 1
        print(a2, b2)


if __name__ == '__main__':
    main()
