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
    n, k, a = inp()
    cur = a - 1
    for i in range(k):
        cur += 1
        if cur > n:
            cur = 1

    print(cur)


if __name__ == '__main__':
    main()
