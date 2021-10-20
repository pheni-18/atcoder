# https://atcoder.jp/contests/abc134/tasks/abc134_e

# DP Others


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
    from collections import deque
    from bisect import bisect_left
    n = inp_one()
    al = [inp_one() for _ in range(n)]

    dq = deque()
    dq.append(al[0])
    for i in range(1, n):
        a = al[i]
        if a <= dq[0]:
            dq.appendleft(a)
        else:
            cur = bisect_left(dq, a)
            dq[cur - 1] = a

    print(len(dq))


if __name__ == '__main__':
    main()
