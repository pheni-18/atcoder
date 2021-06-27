def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    a, b, c = inp()
    ansl = []
    ansl.append(a + b)
    ansl.append(c + b)
    ansl.append(a + c)

    print(max(ansl))


if __name__ == '__main__':
    main()
