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
