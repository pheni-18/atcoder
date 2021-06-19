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
    n = inp()[0]
    al = inp()

    if n == 1:
        print(0)
        return

    to = [-1] * ((2 * 100000) + 1)

    cur = len(al) // 2
    if len(al) % 2 == 0:
        mae = al[:cur]
        ushiro = al[cur:]
    else:
        mae = al[:cur]
        ushiro = al[cur+1:]

    ushiro = list(reversed(ushiro))

    ans = 0
    for i in range(cur):
        m = mae[i]
        im = m
        u = ushiro[i]
        iu = u

        if m == u:
            continue

        while True:
            t = to[m]
            if t == -1:
                if im != m:
                    to[im] = m
                break
            m = t

        while True:
            t = to[u]
            if t == -1:
                if iu != u:
                    to[iu] = u
                break
            u = t

        if m == u:
            continue

        to[m] = u
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
