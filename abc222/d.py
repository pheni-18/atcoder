def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    al = inp()
    bl = inp()

    x = 3001

    m = [[0] * x for _ in range(n + 1)]

    for i in range(n):
        a = al[i]
        b = bl[i]
        for j in range(a, b + 1):
            m[i + 1][j] = 1

    for i in range(1, x):
        m[1][i] += m[1][i - 1]

    for i in range(2, n + 1):
        for j in range(1, x):
            if m[i][j] == 1:
                m[i][j] = (m[i - 1][j] + m[i][j - 1]) % 998244353
            if m[i][j] == 0:
                m[i][j] = (m[i][j - 1]) % 998244353

    print((m[n][3000]) % 998244353)


if __name__ == '__main__':
    main()
