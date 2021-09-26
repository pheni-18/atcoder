def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    al = inp()
    x = inp()[0]

    tot_a = sum(al)
    ans = (x // tot_a) * n
    amari = x % tot_a
    for i in range(n):
        if amari < 0:
            break

        v = al[i]
        amari -= v
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
