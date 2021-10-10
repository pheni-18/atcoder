def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, m = inp()
    all = []
    for _ in range(2 * n):
        al = inp(False)[0]
        all.append(list(al))

    h = [{'no': i, 'win_num': 0} for i in range(2 * n)]

    def f(a, b):
        if a == b:
            return 0
        elif a == 'G':
            if b == 'C':
                return 1
            elif b == 'P':
                return 2
        elif a == 'C':
            if b == 'G':
                return 2
            elif b == 'P':
                return 1
        elif a == 'P':
            if b == 'G':
                return 1
            elif b == 'C':
                return 2

    for i in range(m):
        h = sorted(h, key=lambda x: (x['win_num'], x['no']))
        for j in range(0, 2 * n, 2):
            a = h[j]
            b = h[j + 1]

            a_no = a['no']
            b_no = b['no']
            result = f(all[a_no][i], all[b_no][i])
            if result == 1:
                a['win_num'] -= 1
            elif result == 2:
                b['win_num'] -= 1

    h = sorted(h, key=lambda x: (x['win_num'], x['no']))
    for x in h:
        print(x['no'] + 1)


if __name__ == '__main__':
    main()
