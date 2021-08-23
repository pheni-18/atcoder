def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]

    k = 0
    while True:
        x = 2 ** k
        if x > n:
            print(k - 1)
            break

        k += 1


if __name__ == '__main__':
    main()
