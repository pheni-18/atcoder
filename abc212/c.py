def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from bisect import bisect_left
    n, m = inp()
    al = inp()
    al = sorted(al)
    bl = inp()
    bl = sorted(bl)

    ans = 1001001001
    for i in range(n):
        a = al[i]
        j = bisect_left(bl, a)
        if j == 0:
            ans = min(ans, abs(bl[j] - a))
            continue
        if j == m:
            ans = min(ans, abs(bl[j - 1] - a))
            continue

        ans = min(ans, abs(bl[j] - a), abs(bl[j - 1] - a))

    print(ans)


if __name__ == '__main__':
    main()
