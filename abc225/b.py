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
    n = inp_one()
    abl = [inp() for _ in range(n - 1)]

    cnt = [0] * n
    for a, b in abl:
        a -= 1
        b -= 1
        cnt[a] += 1
        cnt[b] += 1

    for c in cnt:
        if c == n - 1:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
