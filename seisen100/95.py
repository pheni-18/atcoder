# https://atcoder.jp/contests/abc149/tasks/abc149_b

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
    A, B, K = inp()
    if K >= A + B:
        print(0, 0)
        return
    if A >= K:
        print(A - K, B)
        return
    print(0, B - (K - A))


if __name__ == '__main__':
    main()
