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
    x = inp_one()

    if x == 0:
        print('No')
        return

    if x % 100 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
