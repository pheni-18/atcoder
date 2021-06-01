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
    n = inp(True)
    max1 = 0
    max1_i = -1
    max2 = 0
    for i in range(n):
        a = inp(True)
        if a >= max1:
            max2 = max1
            max1 = a
            max1_i = i
        elif a > max2:
            max2 = a

    for i in range(n):
        if i == max1_i:
            print(max2)
        else:
            print(max1)


if __name__ == '__main__':
    main()
