# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d

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
    m = inp()[0]
    mxy_l = []
    for _ in range(m):
        mxy = inp()
        mxy_l.append(mxy)

    nxy_se = set()
    nxy_l = []
    n = inp()[0]
    for _ in range(n):
        x, y = inp()
        nxy_se.add((x, y))
        nxy_l.append([x, y])

    rel_dist_l = []
    for i in range(m - 1):
        x = mxy_l[i + 1][0] - mxy_l[i][0]
        y = mxy_l[i + 1][1] - mxy_l[i][1]
        rel_dist = [x, y]
        rel_dist_l.append(rel_dist)

    ans_x = 0
    ans_y = 0

    for i in range(n):
        xy = nxy_l[i]
        for j in range(m - 1):
            rdx = rel_dist_l[j][0]
            rdy = rel_dist_l[j][1]
            x = xy[0] + rdx
            y = xy[1] + rdy
            xy = [x, y]
            if (x, y) not in nxy_se:
                break
        else:
            ans_x = xy[0] - mxy_l[-1][0]
            ans_y = xy[1] - mxy_l[-1][1]

    print(ans_x, ans_y)


if __name__ == '__main__':
    main()
