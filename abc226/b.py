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
    ll = []
    all = []
    for _ in range(N):
        x = inp()
        l = x[0]
        al = x[1:]
        ll.append(l)
        all.append(al)

    se = set()
    for i in range(N):
        al = all[i]
        s = ''
        for a in al:
            as_ = str(a)
            s += as_.zfill(10)
        se.add(s)

    print(len(se))


if __name__ == '__main__':
    main()
