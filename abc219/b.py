def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    s1 = inp(False)[0]
    s2 = inp(False)[0]
    s3 = inp(False)[0]
    sl = [s1, s2, s3]
    t = inp(False)[0]

    tl = list(map(lambda x: int(x), list(t)))

    ans = ''
    for i in tl:
        ans += sl[i - 1]

    print(ans)


if __name__ == '__main__':
    main()
