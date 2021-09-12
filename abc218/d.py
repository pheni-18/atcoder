def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]

    xd = {}
    yd = {}
    xyl = []
    for _ in range(n):
        x, y = inp()
        xyl.append([x, y])
        if xd.get(x) is None:
            xd[x] = {y}
        else:
            xd[x].add(y)

        if yd.get(y) is None:
            yd[y] = {x}
        else:
            yd[y].add(x)

    cnt = 0
    for x1, y1 in xyl:
        y2 = y1
        x2_c = yd[y1]
        for x2 in x2_c:
            if x1 >= x2:
                continue

            y3_c = xd[x2]
            for y3 in y3_c:
                if y2 >= y3:
                    continue

                if x1 in yd[y3]:
                    cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
