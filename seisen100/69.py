# https://atcoder.jp/contests/abc084/tasks/abc084_d

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


def is_prime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if i * i > n:
            break

        if n % i == 0:
            return False

    return True


def main():
    Q = inp_one()
    lrl = [inp() for _ in range(Q)]

    cnts = [0] * (10 ** 5 + 1)
    for i in range(3, 10 ** 5 + 1, 2):
        prev = cnts[i - 2]
        cnts[i - 1] = prev
        cnts[i] = prev
        if is_prime(i) and is_prime((i + 1) // 2):
            cnts[i] += 1

    for lr in lrl:
        l, r = lr
        ans = cnts[r] - cnts[l - 1]
        print(ans)


if __name__ == '__main__':
    main()
