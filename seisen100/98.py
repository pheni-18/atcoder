# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e

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
    al = inp()
    
    map_= [0] * (N + 1)
    map_[0] = 3
    ans = 1
    for a in al:
        if map_[a] == 0:
            print(0)
            return

        ans *= map_[a]
        ans %= 10 ** 9 + 7

        map_[a] -= 1
        map_[a + 1] += 1

    print(ans)


if __name__ == '__main__':
    main()
