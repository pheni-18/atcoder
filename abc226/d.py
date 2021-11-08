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
    N = inp_one()
    xyl = [inp() for _ in range(N)]

    se = set()

    zumi = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            si = str(i).zfill(3)
            sj = str(j).zfill(3)
            lll = [si, sj]
            lll = sorted(lll)
            aaa = ''.join(lll)
            if aaa in zumi:
                continue
            zumi.add(aaa)
            x1, y1 = xyl[i]
            x2, y2 = xyl[j]
            xd = x1 - x2
            yd = y1 - y2
            xd += 1000000000
            yd += 1000000000
            xs = str(xd)
            ys = str(yd)
            s = xs.zfill(10) + ys.zfill(10)
            se.add(s)

    ans = len(se) * 2
    print(ans)


if __name__ == '__main__':
    main()
