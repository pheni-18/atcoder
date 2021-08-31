def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    a, b = inp()
    min_ = a * 1
    max_ = a * 6
    if min_ <= b <= max_:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
