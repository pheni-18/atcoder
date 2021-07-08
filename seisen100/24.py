# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja

# DFS


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
    vll = [[] for _ in range(n)]
    for _ in range(n):
        l = inp()
        u = l[0] - 1
        vll[u].extend(l[2:])

    time = 0
    ansl = [{'d': 0, 'f': 0} for _ in range(n)]

    def dfs(u):
        if not ansl[u]['d'] == 0:
            return

        nonlocal time
        time += 1

        ansl[u]['d'] = time
        vl = vll[u]
        for v in vl:
            v -= 1
            dfs(v)

        time += 1
        ansl[u]['f'] = time

    for i in range(n):
        if ansl[i]['d'] == 0:
            dfs(i)

    for i in range(n):
        ans = ansl[i]
        print(i + 1, ans['d'], ans['f'])


if __name__ == '__main__':
    main()
