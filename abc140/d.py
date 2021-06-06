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
    n, k = inp()
    s = inp(False)[0]
    sl = list(s)

    cur = sl[0]
    rev_cnt = 0
    ans = 0
    for i in range(n):
        if i + 1 < n:
            if sl[i] == sl[i + 1]:
                ans += 1
        if rev_cnt // 2 >= k:
            continue
        if cur != sl[i]:
            cur = sl[i]
            rev_cnt += 1
            if rev_cnt % 2 == 0:
                ans += 2
    else:
        if rev_cnt % 2 == 1:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
