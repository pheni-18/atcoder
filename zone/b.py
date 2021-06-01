def inp(to_int=False):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    l = sl2il(l) if to_int else l
    return l[0] if len(l) == 1 else l


def inps(n, to_int=False):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def sl2il(l):
    return list(map(lambda x: int(x), l))


def il2sl(l):
    return list(map(lambda x: str(x), l))


def main():
    n, D, H = inp(True)
    dhl = inps(n, True)
    dhl2 = list(dhl)
    ans = 1000
    for dh in dhl:
        a = (H - dh[1]) / (D - dh[0])
        b = H - (D * a)
        if b < 0:
            b = 0
            a = H / D
        for dh2 in dhl2:
            y = a * dh2[0] + b
            if dh2[1] > y:
                break
        else:
            if b < ans:
                ans = b
    print(ans)


if __name__ == '__main__':
    main()
