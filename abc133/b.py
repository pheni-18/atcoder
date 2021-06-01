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
    n, d = inp(True)
    xl = inps(n, True)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            wa = 0
            if d == 1:
                wa += (xl[i] - xl[j]) ** 2
                for l in range(130):
                    if l ** 2 == wa:
                        ans += 1
                        break
                continue
            for k in range(d):
                wa += (xl[i][k] - xl[j][k]) ** 2
            for l in range(130):
                if l ** 2 == wa:
                    ans += 1
                    break
    print(ans)


if __name__ == '__main__':
    main()
