def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    x = inp(False)[0]
    n = inp()[0]
    sl = [inp(False)[0] for _ in range(n)]

    d = {}
    for i in range(1, 27):
        d[x[i - 1]] = i

    name_d = {}

    name_nol = []
    for s in sl:
        name_nos = ''
        for i in range(10):
            if i <= len(s) - 1:
                c = list(s)[i]
                x = str(d[c])
            else:
                x = str(0)
            xs = x.zfill(2)
            name_nos += xs

        name_no = int(name_nos)
        name_nol.append(name_no)
        name_d[name_no] = s

    name_nol = sorted(name_nol)

    for name_no in name_nol:
        name = name_d[name_no]
        print(name)


if __name__ == '__main__':
    main()
