# https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a

# 累積和


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
    N = inp_one()
    al = inp()

    total = [0]
    for i in range(N):
        a = al[i]
        total.append(total[i] + a)

    for k in range(1, N + 1):
        ans = 0
        for i in range(1, N - k + 2):
            v = total[i + k - 1] - total[i - 1]
            ans = max(ans, v)

        print(ans)


if __name__ == '__main__':
    main()
