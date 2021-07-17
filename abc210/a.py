def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, a, x, y = inp()
    if n >= a:
        ans = a * x + (n - a) * y
    else:
        ans = n * x

    print(ans)


if __name__ == '__main__':
    main()
