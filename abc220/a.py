def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    a, b, c = inp()
    v = c
    ans = -1
    while v <= b:
        if a <= v <= b:
            ans = v
            break

        v += v

    print(ans)


if __name__ == '__main__':
    main()
