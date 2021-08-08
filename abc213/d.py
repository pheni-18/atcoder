def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import sys
    sys.setrecursionlimit(4 * (10 ** 5))

    n = inp()[0]
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    for i in range(n):
        t = to[i]
        to[i] = sorted(t)

    def dfs(u, f):
        print(u + 1)
        for v in to[u]:
            if f == v:
                continue

            dfs(v, u)
            print(u + 1)

    dfs(0, None)


if __name__ == '__main__':
    main()
