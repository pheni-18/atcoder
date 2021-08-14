def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    if 1 <= n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)


if __name__ == '__main__':
    main()
