# https://atcoder.jp/contests/abc139/tasks/abc139_d

# 数学的な問題


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
    m = N - 1
    ans = m * (m + 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
