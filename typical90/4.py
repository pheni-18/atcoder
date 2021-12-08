# ☆2

#

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
    H, W = inp()
    all = [inp() for _ in range(H)]

    h_total = []
    for i in range(H):
        al = all[i]
        h_total.append(sum(al))

    w_total = []
    for j in range(W):
        p = 0
        for i in range(H):
              p += all[i][j]
        w_total.append(p)

    for i in range(H):
        l = []
        for j in range(W):
            ans = h_total[i] + w_total[j] - all[i][j]
            l.append(ans)

        print(*l)


if __name__ == '__main__':
    main()
