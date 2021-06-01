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

    l = list(s)

    kouho = []
    for i in range(10000):
        si = str(i).zfill(4)
        s1, s2, s3, s4 = list(si)
        i1 = int(s1)
        i2 = int(s2)
        i3 = int(s3)
        i4 = int(s4)
        if l[i1] != 'x' and l[i2] != 'x' and l[i3] != 'x' and l[i4] != 'x':
            kouho.append(si)

    ansl = []
    for ko in kouho:
        for i, x in enumerate(l):
            if x == 'o':
                if str(i) not in list(ko):
                    break
        else:
            ansl.append(ko)

    print(len(ansl))



if __name__ == '__main__':
    main()
