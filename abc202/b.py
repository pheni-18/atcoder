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
    s = inp(False)[0]
    sl = list(s)
    rev_sl = list(reversed(sl))

    for i in range(len(rev_sl)):
        if rev_sl[i] == '6':
            rev_sl[i] = '9'
        elif rev_sl[i] == '9':
            rev_sl[i] = '6'

    print(''.join(rev_sl))


if __name__ == '__main__':
    main()
