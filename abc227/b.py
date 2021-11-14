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
    sl = inp()

    se = set()
    for a in range(1, 1000):
        for b in range(1, 1000):
            s = 4 * a * b + 3 * a + 3 * b
            if s <= 1000:
                se.add(s)

    ans = 0
    for s in sl:
        if s not in se:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
