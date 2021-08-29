def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    names = [inp(False) for _ in range(n)]
    flg = False
    for i in range(n):
        for j in range(i + 1, n):
            s1, t1 = names[i]
            s2, t2 = names[j]
            if s1 == s2 and t1 == t2:
                flg = True

    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
