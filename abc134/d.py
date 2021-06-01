def inp(to_int=False):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return sl2il(l) if to_int else l


def inps(n, to_int=False):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def sl2il(l):
    return list(map(lambda x: int(x), l))


def il2sl(l):
    return list(map(lambda x: str(x), l))


def main():
    n = inp(True)[0]
    al = inp(True)

    hako = [0] * n
    for i in reversed(range(n)):
        j = 1
        wa = 0
        while (i + 1) * j - 1 < n:
            k = (i + 1) * j - 1
            wa += hako[k]
            j += 1

        if wa % 2 == al[i]:
            hako[i] = 0
        else:
            hako[i] = 1

    m = hako.count(1)
    print(m)

    bl = []
    if not m == 0:
        for i in range(n):
            if hako[i] == 1:
                bl.append(str(i+1))

    if not bl == []:
        print(' '.join(bl))


if __name__ == '__main__':
    main()
