def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inp_one(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    s = input()
    return int(s) if to_int else s


def main():
    N = inp_one()
    
    ans = 0
    i = 1
    while i <= N:
        x = N // i
        ni = N // x + 1
        ans += x * (ni - i)
        i = ni

    print(ans)


if __name__ == '__main__':
    main()
