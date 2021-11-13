# https://qiita.com/e869120/items/eb50fdaece12be418faa

# 素数判定


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


def prime_factorize(n):
    l = []
    m = n
    for a in range(2, n):
        if a * a > n:
            break

        if m % a != 0:
            continue

        ex = 0
        while m % a == 0:
            ex += 1
            m //= a

        l.append((a, ex))

    if m != 1:
        l.append((m, 1))

    return l


def main():
    n = inp_one()

    l = prime_factorize(n)
    ans = f'{n}:'
    for t in l:
        a, ex = t
        for _ in range(ex):
            ans += f' {a}'

    print(ans)


if __name__ == '__main__':
    main()
