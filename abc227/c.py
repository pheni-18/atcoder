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
    ans = 0
    for a in range(1, 10 ** 4):
        for b in range(a, 10 ** 6):
            m = N // (a * b)
            if m < b:
                break
            ans += m - (b - 1)

    print(ans)


if __name__ == '__main__':
    main()
