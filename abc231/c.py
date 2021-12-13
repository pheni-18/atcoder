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
    from bisect import bisect_left

    N, Q = inp()
    al = inp()
    xl = [inp_one() for _ in range(Q)]

    al = sorted(al)
    len_al = len(al)
    for x in xl:
        cur = bisect_left(al, x)
        
        print(len_al - cur)


if __name__ == '__main__':
    main()
