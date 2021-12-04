# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_d

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
    
    if N == 1:
        print('Yes')
        print(2)
        print(1, 1)
        print(1, 1)
        return

    K = 0
    for k in range(10 ** 3):
        if 2 * N == k * (k - 1):
            K = k
        
    if K == 0:
        print('No')
        return

    print('Yes')
    print(K)

    l = 1
    ansll = []
    ansl2 = [K - 1]
    cur = 0
    for sa in range(1, N):
        cur += sa
        if cur > N:
            break
        ansl = [K - 1, cur]
        ansl += [i for i in range(l, cur)]
        cur2 = cur
        for sa2 in range(sa, N):
            cur2 += sa2
            if cur2 > N:
                break
            ansl.append(cur2)

        ansl2.append(cur)
        ansll.append(ansl)
        l = cur + 1

    ansll.append(ansl2)

    for ansl in ansll:
        print(*ansl)


if __name__ == '__main__':
    main()
