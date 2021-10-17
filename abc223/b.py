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
    s = inp_one(False)
    l = []
    now = list(s)
    for _ in range(len(s)):
        a = now.pop(0)
        now.append(a)
        l.append(''.join(now))

    l = sorted(l)
    print(l[0])
    print(l[-1])


if __name__ == '__main__':
    main()
