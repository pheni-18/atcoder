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
    a, b, k = inp()

    c = [[0] * 61 for _ in range(61)]
    c[0][0] = 1
    for i in range(60):
        for j in range(i+1):
            c[i+1][j] += c[i][j]
            c[i+1][j+1] += c[i][j]

    ans = ''
    while a + b > 0:
        x = 0
        if a >= 1:
            x = c[a+b-1][a-1]

        if k <= x:
            ans += 'a'
            a -= 1
        else:
            ans += 'b'
            b -= 1
            k -= x

    print(ans)


if __name__ == '__main__':
    main()
