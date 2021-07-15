# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d

# DFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import sys
    sys.setrecursionlimit(10 ** 4)

    m = inp()[0]
    n = inp()[0]
    sll = []
    for _ in range(n):
        sl = inp()
        sll.append(sl)

    ans = 0
    cnt = 0
    visited = [[0] * m for _ in range(n)]

    def dfs(y, x):
        nonlocal ans
        nonlocal cnt

        cnt += 1
        visited[y][x] = 1
        for d in [1, -1]:
            if not (0 <= y + d < n):
                continue

            if sll[y + d][x] == 0:
                continue

            if visited[y + d][x] == 1:
                continue

            dfs(y + d, x)

        for d in [1, -1]:
            if not (0 <= x + d < m):
                continue

            if sll[y][x + d] == 0:
                continue

            if visited[y][x + d] == 1:
                continue

            dfs(y, x + d)

        ans = max(ans, cnt)
        cnt -= 1
        visited[y][x] = 0

    for i in range(n):
        for j in range(m):
            if sll[i][j] == 0:
                continue

            dfs(i, j)

    print(ans)


if __name__ == '__main__':
    main()
