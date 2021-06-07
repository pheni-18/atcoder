# https://atcoder.jp/contests/abc122/tasks/abc122_b

def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    s = inp(False)[0]
    sl = list(s)

    ansl = [0]
    cnt = 0
    for i in range(len(sl)):
        if sl[i] in ['A', 'C', 'G', 'T']:
            cnt += 1
        else:
            ansl.append(cnt)
            cnt = 0
    else:
        ansl.append(cnt)

    print(max(ansl))


if __name__ == '__main__':
    main()
