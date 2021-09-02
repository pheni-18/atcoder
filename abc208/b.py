def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import math
    p = inp()[0]
    coins = []
    for i in range(1, 11):
        x = math.factorial(i)
        coins.append(x)

    coins = reversed(coins)

    ans = 0
    for coin in coins:
        ans += p // coin
        p %= coin

    print(ans)


if __name__ == '__main__':
    main()
