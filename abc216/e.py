def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, k = inp()
    al = inp()
    al = sorted(al, reverse=True)

    cnt = 0
    cur = 1

    def get_sa(n):
        return (1 / 2) * n * (n + 1)

    if n == 1:
        if k >= al[0]:
            print(get_sa(al[0]))
            return
        b = al[0] - k
        ans = get_sa(al[0] - get_sa(b))
        print(ans)
        return





if __name__ == '__main__':
    main()
