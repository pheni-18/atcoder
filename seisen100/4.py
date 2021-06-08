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
    n, m = inp()

    all = []
    for _ in range(n):
        all.append(inp())

    ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            total = 0
            for k in range(n):
                total += max(all[k][i], all[k][j])
            if total > ans:
                ans = total

    print(ans)


if __name__ == '__main__':
    main()
