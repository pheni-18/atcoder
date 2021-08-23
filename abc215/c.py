def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from itertools import permutations

    s, k = inp(False)
    k = int(k)

    sl = []
    for t in permutations(list(s)):
        sl.append(''.join(t))

    sl = sorted(sl)
    p = ''
    cnt = 0
    for s2 in sl:
        if p == s2:
            continue

        cnt += 1
        if cnt == k:
            print(s2)
            break

        p = s2


if __name__ == '__main__':
    main()
