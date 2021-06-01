def inp(i, to_int=False):
    l = [input().split() for _ in range(i)]
    l = list(map(lambda x: sl2il(x), l)) if to_int else l
    return l[0] if i == 1 else l


def sl2il(l):
    return list(map(lambda x: int(x), l))


def il2sl(l):
    return list(map(lambda x: str(x), l))


def main():
    n = inp(1, True)[0]
    dl = sorted(inp(1, True))

    dlen = len(dl)
    i = dlen // 2
    ans = dl[i] - dl[i-1]
    print(ans)


if __name__ == '__main__':
    main()
