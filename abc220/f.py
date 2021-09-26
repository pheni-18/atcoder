def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = inp()
        u -= 1
        v -= 1
        to[u].append(v)
        to[v].append(u)


if __name__ == '__main__':
    main()
