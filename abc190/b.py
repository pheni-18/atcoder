def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, s, d = inp()
    xyl = [inp() for _ in range(n)]

    ans = 'No'
    for x, y in xyl:
        if x < s and y > d:
            ans = 'Yes'

    print(ans)


if __name__ == '__main__':
    main()
