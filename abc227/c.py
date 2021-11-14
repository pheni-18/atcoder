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
    N, K = inp()
    al = inp()

    al = sorted(al)
    cur1 = N - K
    ans = 0
    cur2 = N - 1
    while True:
        ans += al[cur1]
        al[cur2] -= al



if __name__ == '__main__':
    main()
