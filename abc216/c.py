def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    v = n
    ansl = []
    for _ in range(120):
        if v % 2 == 0:
            v = v // 2
            ansl.append('B')
        else:
            v -= 1
            ansl.append('A')

        if v == 0:
            break

    ansl = reversed(ansl)
    print(''.join(ansl))


if __name__ == '__main__':
    main()
