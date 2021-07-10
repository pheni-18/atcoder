# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

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
    import sys
    sys.setrecursionlimit(2501)

    wl = []
    hl = []
    clll = []
    while True:
        w, h = inp()
        if w == 0 and h == 0:
            break

        wl.append(w)
        hl.append(h)

        cll = []
        for _ in range(h):
            cl = inp()
            cll.append(cl)

        clll.append(cll)

    for w, h, cll in zip(wl, hl, clll):
        visited = [[0] * w for _ in range(h)]

        ans = 0

        def dfs(y, x):
            if cll[y][x] == 0:
                return

            if visited[y][x] == 1:
                return

            visited[y][x] = 1

            for dy in [0, 1, -1]:
                for dx in [0, 1, -1]:
                    if dy == 0 and dx == 0:
                        continue

                    vy = y + dy
                    vx = x + dx
                    nonlocal h
                    nonlocal w
                    if (0 <= vy < h) and (0 <= vx < w):
                        dfs(vy, vx)

        for i in range(h):
            for j in range(w):
                if cll[i][j] == 1 and visited[i][j] == 0:
                    dfs(i, j)
                    ans += 1

        print(ans)


if __name__ == '__main__':
    main()
