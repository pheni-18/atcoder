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
    end = [[] for _ in range(n)]

    if m == 0:
        print(n)

    for i in range(m):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)

    def dfs(f, j):
        for v in to[f]:
            if v in end[j]:
                continue

            if len(end[v]) > 0:
                end[j].extend(end[v])
                continue

            end[j].append(v)
            dfs(v, j)

    for j in range(n):
        end[j].append(j)
        dfs(j, j)

    ans = 0
    for i in range(n):
        ans += len(end[i])

    print(ans)


if __name__ == '__main__':
    main()
