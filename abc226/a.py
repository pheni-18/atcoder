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
    X = inp_one(False)
    x, y = X.split('.')
    if int(y[0]) >= 5:
        print(int(x) + 1)
    else:
        print(x)


if __name__ == '__main__':
    main()
