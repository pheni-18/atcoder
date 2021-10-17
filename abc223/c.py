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

    m_len = 0
    abl = []
    for _ in range(n):
        a, b = inp()
        m_len += a
        abl.append([a, b])

    l_cur = 0
    r_cur = len(abl) - 1
    lt = 0
    rt = 0
    ll = 0
    rl = 0

    if n == 1:
        print(m_len / 2)
        return

    while True:
        la, lb = abl[l_cur]
        ra, rb = abl[r_cur]

        prev_ll = ll
        prev_rl = rl
        ll += la
        rl += ra

        prev_lt = lt
        prev_rt = rt
        lt = lt + (la / lb)
        rt = rt + (ra / rb)

        if ll + rl >= m_len:
            if lt == rt:
                ans = ll
            elif lt < rt:
                pt = rt - lt
                ans = ll + (rb * (pt / 2))
            else:
                pt = lt - rt
                ans = m_len - (rl + (lb * (pt / 2)))

            break

        if lt > rt:
            r_cur -= 1
            lt = prev_lt
            ll = prev_ll
        else:
            l_cur += 1
            rt = prev_rt
            rl = prev_rl

    print(ans)


if __name__ == '__main__':
    main()
