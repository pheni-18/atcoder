def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    v = inp(False)[0]
    x, y = v.split('.')
    x = int(x)
    y = int(y)

    if 0 <= y <= 2:
        print(str(x) + '-')
    if 3 <= y <= 6:
        print(str(x))
    if 7 <= y <= 9:
        print(str(x) + '+')


if __name__ == '__main__':
    main()
