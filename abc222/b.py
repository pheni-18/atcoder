def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, p = inp()
    al = inp()
    ans = 0
    for a in al:
        if a < p:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
