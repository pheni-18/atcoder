# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_a

# 連長圧縮


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
    cl = [inp_one() for _ in range(n)]

    counts = [0] * n
    counts[0] = 1
    prev_c = cl[0]
    idx = 0

    for i in range(2, n + 1):
        c = cl[i - 1]
        if i % 2 == 1:
            if prev_c == c:
                counts[idx] += 1
            else:
                idx += 1
                counts[idx] += 1
        else:
            if prev_c == c:
                counts[idx] += 1
            else:
                if idx == 0:
                    counts[idx] += 1
                else:
                    counts[idx - 1] += counts[idx] + 1
                    counts[idx] = 0
                    idx -= 1
        
        prev_c = c

    o = 0
    e = 0
    for i in range(idx + 1):
        if i % 2 == 1:
            o += counts[i]
        else:
            e += counts[i]
        
    if idx % 2 == 1:
        if prev_c == 0:
            ans = o
        else:
            ans = e
    else:
        if prev_c == 0:
            ans = e
        else:
            ans = o

    print(ans)


if __name__ == '__main__':
    main()
