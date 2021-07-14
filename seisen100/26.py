# https://atcoder.jp/contests/abc138/tasks/abc138_d

# DFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import sys
    sys.setrecursionlimit(4 * (10 ** 5))

    n, q = inp()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    xl = [0] * n
    for _ in range(q):
        p, x = inp()
        p -= 1
        xl[p] += x

    scores = [0] * n

    def dfs(u, f, x):
        for v in to[u]:
            if f == v:
                continue

            x += xl[v]
            dfs(v, u, x)
            x -= xl[v]

        scores[u] = x

    dfs(0, -1, xl[0])

    for s in scores:
        print(s)


if __name__ == '__main__':
    main()
