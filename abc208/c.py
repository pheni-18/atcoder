def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, k = inp()
    al = inp()
    pl = []
    for i in range(n):
        a = al[i]
        pl.append({'i': i, 'a': a, 'c': 0})

    pl = sorted(pl, key=lambda x: x['a'])
    r = k % n
    for i in range(n):
        pl[i]['c'] += k // n
        if i < r:
            pl[i]['c'] += 1

    pl = sorted(pl, key=lambda x: x['i'])
    for p in pl:
        print(p['c'])


if __name__ == '__main__':
    main()
