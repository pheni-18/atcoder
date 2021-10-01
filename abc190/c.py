def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from itertools import product

    n, m = inp()
    abl = [inp() for _ in range(m)]
    k = inp()[0]
    cdl = [inp() for _ in range(k)]

    ans = 0
    for _bit in product((True, False), repeat=k):
        pl = [False for _ in range(n + 1)]
        for i in range(k):
            c, d = cdl[i]
            if _bit[i]:
                pl[c] = True
            else:
                pl[d] = True

        cnt = 0
        for i in range(m):
            a, b = abl[i]
            if pl[a] and pl[b]:
                cnt += 1

        ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
