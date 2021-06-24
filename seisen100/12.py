# https://atcoder.jp/contests/abc002/tasks/abc002_4

# bit全探索


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
    from itertools import product

    n, m = inp()
    if m == 0:
        print(1)
        return

    relations = [[] for _ in range(n)]
    for i in range(m):
        x, y = inp()
        x -= 1
        y -= 1
        relations[x].append(y)
        relations[y].append(x)

    ans = 0
    for _bit in product((True, False), repeat=n):
        bit = list(_bit)
        cnt = 0
        for i in range(n):
            if not bit[i]:
                continue

            for j in range(n):
                if i == j or not bit[j]:
                    continue

                if j not in relations[i]:
                    break
            else:
                cnt += 1

        if bit.count(True) == cnt:
            ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
