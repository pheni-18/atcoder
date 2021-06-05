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
    s = inp(False)[0]
    t = inp(False)[0]

    ans = 0
    for i in range(3):
        if s[i] == t[i]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
