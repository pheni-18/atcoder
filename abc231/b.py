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
    sl = [inp_one(False) for _ in range(N)]

    d = {}
    for s in sl:
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1

    ans = ''
    p = 0
    for k, v in d.items():
        if v > p:
            ans = k
            p = v

    print(ans)


if __name__ == '__main__':
    main()
