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
    N, D = inp()
    lrl = [inp() for _ in range(N)]

    lrl = sorted(lrl, key=lambda x: x[1])
    cnt = 0
    cur = 0
    for l, r in lrl:
        if l > cur:
            cur = r + D - 1
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
