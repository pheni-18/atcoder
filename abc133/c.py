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
    l, r = inp(True)
    r = min([r, l + 4038])
    ans = 2020
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            m = (i * j) % 2019
            if m < ans:
                ans = m
    print(ans)


if __name__ == '__main__':
    main()
