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
    import sys
    sys.setrecursionlimit(1001001)

    def dfs(f, p):
        for v in to[f]:
            if v == p:
                continue

            ansl[v] += ansl[f]
            dfs(v, f)

    n, q = inp()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    ansl = [0] * n
    for _ in range(q):
        p, x = inp()
        p -= 1
        ansl[p] += x

    dfs(0, None)

    ansl = list(map(lambda x: str(x), ansl))
    print(' '.join(ansl))


if __name__ == '__main__':
    main()
