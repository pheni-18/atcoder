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
    sys.setrecursionlimit(4000001)
    n, m = inp()

    to = [[] for _ in range(n)]
    for _ in range(m):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)

    def dfs(f):
        nonlocal ans
        nonlocal seen

        ans += 1
        seen[f] = True

        for v in to[f]:
            if seen[v]:
                continue
            dfs(v)

    ans = 0
    for i in range(n):
        seen = [False] * n
        dfs(i)

    print(ans)


if __name__ == '__main__':
    main()
