def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    h, w, c = inp()
    all = []
    for _ in range(h):
        al = inp()
        all.append(al)

    ac = 0
    wa = 3 * (10 ** 12)
    while ac + 1 < wa:
        wj = (ac + wa) // 2


    print(ac)


if __name__ == '__main__':
    main()
