def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    s = inp(False)[0]

    if s[n - 1] == 'o':
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
