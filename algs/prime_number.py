# 素数判定

def is_prime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if i * i > n:
            break

        if n % i == 0:
            return False

    return True


# 約数列挙

def count_divisors(n: int) -> int:
    l = []
    for i in range(1, n):
        if i * i > n:
            break

        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n // i)

    l = sorted(l)
    return l


# 素因数分解

def prime_factorize(n: int) -> list[tuple[int: int]]:
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
