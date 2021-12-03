def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inp_one(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    s = input()
    return int(s) if to_int else s


def main():
    N, A, B = inp()
    P, Q, R, S = inp()

    k1_min = max(1 - A, 1 - B)
    k1_max = min(N - A, N - B)
    k2_min = max(1 - A, B - N)
    k2_max = min(N - A, B - 1)

    for i in range(P, Q + 1):
        s = ''
        for j in range(R, S + 1):
            t = '.'
            if k1_min + A <= i <= k1_max + A:
                k = i - A
                if j == B + k:
                    t = '#'
            if k2_min + A <= i <= k2_max + A:
                k = i - A
                if j == B - k:
                    t = '#'
            s += t
        print(s)


if __name__ == '__main__':
    main()
