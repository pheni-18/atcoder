def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    a, b = inp()
    c = ((a - b) / 3) + b
    print(c)


if __name__ == '__main__':
    main()
