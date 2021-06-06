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
    n = inp()[0]
    bl = inp()
    al = [0] * n
    for i in range(n - 1):
        if i == 0:
            al[i] = bl[i]
            al[i + 1] = bl[i]
            continue

        if bl[i] < bl[i - 1]:
            al[i] = bl[i]

        al[i + 1] = bl[i]

    print(sum(al))

if __name__ == '__main__':
    main()
