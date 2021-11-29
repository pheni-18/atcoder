# https://atcoder.jp/contests/s8pc-5/tasks/s8pc_5_b

# 幾何計算


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
    import math

    N, M = inp()
    cl = []
    for _ in range(N):
        x, y, r = inp()
        cl.append([x, y, r])
    for _ in range(M):
        x, y = inp()
        cl.append([x, y, -1])

    p = float('inf')
    for i in range(N + M):
        x1, y1, r1 = cl[i]
        for j in range(i + 1, N + M):
            x2, y2, r2 = cl[j]
            d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if r1 > 0 and r2 > 0:
                p = min(p, r1, r2)
            elif r1 > 0:
                p = min(p, r1, d - r1)
            elif r2 > 0:
                p = min(p, r2, d - r2)
            else:
                p = min(p, d / 2)

    print(p)


if __name__ == '__main__':
    main()
