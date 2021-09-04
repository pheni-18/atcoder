def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    s, t = inp(False)
    l = [s, t]
    l2 = sorted(l)

    if l == l2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
