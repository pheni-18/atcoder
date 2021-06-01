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
    a = inp()
    b = inp()

    cnt = 0
    for i in range(n):
        if b[i] > a[i]:
            if b[i] - a[i] > a[i + 1]:
                cnt += a[i] + a[i + 1]
                a[i + 1] = 0
            else:
                a[i + 1] = a[i + 1] - b[i] + a[i]
                cnt += b[i]
            a[i] = 0
        else:
            a[i] -= b[i]
            cnt += b[i]

    print(cnt)



if __name__ == '__main__':
    main()
