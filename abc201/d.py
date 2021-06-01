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

    h, w = inp()
    al = inps(h, False)

    for i in range(h):
        al[i] = list(al[i][0])
        for j in range(w):
            al[i][j] = 1 if al[i][j] == '+' else -1

    memo = [[0] * 2005 for _ in range(2005)]
    visited = [[False] * 2005 for _ in range(2005)]

    def f(i, j):
        if i + 1 == h and j + 1 == w:
            return 0
        if visited[i][j]:
            return memo[i][j]

        visited[i][j] = True
        res = -1001001001
        if i + 1 < h:
            res = max(res, al[i+1][j] - f(i+1, j))
        if j + 1 < w:
            res = max(res, al[i][j+1] - f(i, j+1))
        memo[i][j] = res
        return res

    score = f(0, 0)
    if score == 0:
        print('Draw')
    elif score > 0:
        print('Takahashi')
    elif score < 0:
        print('Aoki')


if __name__ == '__main__':
    main()
