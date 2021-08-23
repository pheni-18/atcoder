def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    s = inp(False)[0]
    if s == 'Hello,World!':
        print('AC')
    else:
        print('WA')


if __name__ == '__main__':
    main()
