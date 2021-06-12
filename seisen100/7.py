# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c

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

    es = set()
    xyl = []
    for i in range(1, n + 1):
        x, y = inp()
        xyl.append([x, y])
        es.add((x, y))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = xyl[i]
            x2, y2 = xyl[j]
            vecx, vecy = x2 - x1, y2 - y1
            x3, y3 = [x1 - vecy, y1 + vecx]
            x4, y4 = [x2 - vecy, y2 + vecx]

            if (x3, y3) in es and (x4, y4) in es:
                area = (x1 - x2) ** 2 + (y1 - y2) ** 2
                ans = max(ans, area)

    print(ans)


if __name__ == '__main__':
    main()
