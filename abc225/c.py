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
    n, m = inp()
    bll = []
    for _ in range(n):
        bl = inp()
        bll.append(bl)

    x = (bll[0][0]) % 7
    if x + m > 8:
        print('No')
        return

    if x == 0 and m >= 2:
        print('No')
        return

    for i in range(n):
        for j in range(m):
            if j > 0:
                if not bll[i][j] == bll[i][j - 1] + 1:
                    print('No')
                    return

            if i > 0:
                if not bll[i][j] == bll[i - 1][j] + 7:
                    print('No')
                    return

    print('Yes')


if __name__ == '__main__':
    main()
