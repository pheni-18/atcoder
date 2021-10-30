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
    s = inp_one(False)

    se = set()
    sl = list(s)
    for s in sl:
        se.add(s)

    if len(se) == 1:
        print(1)
    elif len(se) == 2:
        print(3)
    else:
        print(6)


if __name__ == '__main__':
    main()
