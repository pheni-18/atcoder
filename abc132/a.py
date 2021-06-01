def inp(i, to_int=False):
    l = [input().split() for _ in range(i)]
    l = list(map(lambda x: sl2il(x), l)) if to_int else l
    return l[0] if i == 1 else l


def sl2il(l):
    return list(map(lambda x: int(x), l))


def il2sl(l):
    return list(map(lambda x: str(x), l))


def main():
    s = inp(1)[0]
    se = set(s)
    if len(se) != 2:
        print('No')
        return
    l = list(s)
    for x in se:
        if l.count(x) != 2:
            print('No')
            return
    else:
        print('Yes')


if __name__ == '__main__':
    main()
