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
    n, m = inp()
    abl = []
    refl = [{'v': i + 1, 'ref': [], 'c': 0} for i in range(n)]
    for _ in range(m):
        a, b = inp()
        d = refl[b - 1]
        d['ref'].append(a)
        d['c'] += 1
        abl.append([a, b])

    ans = -1

    used = [False for _ in range(n + 1)]
    for ab in abl:


    print(ans)


if __name__ == '__main__':
    main()
