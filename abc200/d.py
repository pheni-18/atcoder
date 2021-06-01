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
    from itertools import product
    n = inp()[0]
    al = inp()
    n = min(8, n)

    ms = [None] * 200
    for bit in product((True, False), repeat=n):
        wa = 0
        for i in range(n):
            if bit[i]:
                wa += al[i]
        if wa == 0:
            continue
        wa %= 200
        if ms[wa] is not None:
            x = 0
            xl = []
            for j in range(n):
                if ms[wa][j]:
                    x += 1
                    xl.append(str(j + 1))

            y = 0
            yl = []
            for j in range(n):
                if bit[j]:
                    y += 1
                    yl.append(str(j + 1))

            print('Yes')
            print(x, ' '.join(xl))
            print(y, ' '.join(yl))
            return
        else:
            ms[wa] = bit
    print('No')






if __name__ == '__main__':
    main()
