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
    cl = inp()

    cl = sorted(cl)
    ans = 1
    for i in range(n):
        if cl[i] < i + 1:
            ans = 0
            break

        ans = (ans * (cl[i] - i)) % (1000000000 + 7)

    print(ans)


if __name__ == '__main__':
    main()
