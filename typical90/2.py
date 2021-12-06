# ☆3

# 


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
    from itertools import product

    N = inp_one()

    ansl = []
    for _bit in product(('(', ')'), repeat=N):
        cnt = 0
        ans = ''
        for s in _bit:
            ans += s
            if s == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    break
        if cnt == 0:
            ansl.append(ans)
                
    ansl = sorted(ansl)
    for ans in ansl:
        print(ans)


if __name__ == '__main__':
    main()
