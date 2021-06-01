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
    s = inp(False)[0]
    sl = list(s)
    n = len(sl)

    ansl = [0] * n
    rcnt = 0
    lcnt = 0
    sep = 0
    mode = 'R'

    for i in range(n):
        if mode == 'R':
            rcnt += 1
        else:
            lcnt += 1

        end = False
        if i >= n - 1:
            end = True
        else:
            if sl[i] == 'R' and sl[i + 1] == 'L':
                sep = i
                mode = 'L'

            if sl[i] == 'L' and sl[i + 1] == 'R':
                mode = 'R'
                end = True

        if end:
            cnt = rcnt + lcnt
            if cnt % 2 == 0:
                ansl[sep] = cnt // 2
                ansl[sep + 1] = cnt // 2
            else:
                if rcnt % 2 == 0:
                    ansl[sep] = cnt // 2
                    ansl[sep + 1] = cnt // 2 + 1
                else:
                    ansl[sep] = cnt // 2 + 1
                    ansl[sep + 1] = cnt // 2

            rcnt = 0
            lcnt = 0

    ansl = [str(x) for x in ansl]
    print(' '.join(ansl))


if __name__ == '__main__':
    main()
