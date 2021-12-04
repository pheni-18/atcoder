# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_d

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
    M = inp_one()
    dcl = [inp() for _ in range(M)]
    
    s = 0
    n = 0
    for d, c in dcl:
        n += c
        s += d * c

    ans = (n - 1) + (s - 1) // 9
    print(ans)


if __name__ == '__main__':
    main()
