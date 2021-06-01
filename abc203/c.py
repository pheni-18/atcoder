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
    n, k = inp()
    abl = []
    for _ in [0] * n:
        a, b = inp()
        abl.append({'a': a, 'b': b})

    abl = sorted(abl, key=lambda x: x['a'])

    now = 0
    now += k
    for i in range(n):
        ab = abl[i]
        if now >= ab['a']:
            now += ab['b']
        else:
            break

    print(now)


if __name__ == '__main__':
    main()
