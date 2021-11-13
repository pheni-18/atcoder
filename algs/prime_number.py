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
