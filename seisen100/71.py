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
    N, Q = inp()
    MOD = 10 ** 9 + 7
    al = [0]
    al.extend(inp())
    cl = inp()

    dists = [0] * (N + 1)
    for i in range(2, N + 1):
        a1 = al[i - 1]
        a2 = al[i]
        dist = pow(a1, a2, MOD)
        dists[i] = dists[i - 1] + dist

    ans = 0
    prev_c = 1
    for c in cl:
        ans += abs(dists[c] - dists[prev_c])
        ans %= MOD
        prev_c = c

    ans += abs(dists[1] - dists[prev_c])
    ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
