def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    k = inp()[0]
    a, b = inp()

    a2 = int(str(a), k)
    b2 = int(str(b), k)

    print(a2 * b2)


if __name__ == '__main__':
    main()
