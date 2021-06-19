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

    tot = 0
    ans = 0
    for i in range(1001001001):
        tot += i
        if tot >= n:
            ans = i
            break

    print(ans)

if __name__ == '__main__':
    main()
