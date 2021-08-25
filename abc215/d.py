def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, m = inp()
    al = inp()
    l = 100001
    xl = [False] * l
    for a in al:
        xl[a] = True

    dl = []
    for i in range(2, l):
        flg = False
        for j in range(i, l, i):
            if xl[j]:
                flg = True
                break

        if flg:
            dl.append(i)

    okl = [True] * (m + 1)
    for d in dl:
        for i in range(d, m + 1, d):
            okl[i] = False

    ansl = []
    for i in range(1, m + 1):
        if okl[i]:
            ansl.append(i)

    print(len(ansl))
    for ans in ansl:
        print(ans)


if __name__ == '__main__':
    main()
