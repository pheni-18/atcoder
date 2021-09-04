def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    p = inp()
    q = [0] * n
    for i in range(n):
        v = p[i]
        q[v - 1] = i + 1

    for v in q:
        print(v)


if __name__ == '__main__':
    main()
