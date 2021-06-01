def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    s = inp(False)[0]

    f = int(s[:2])
    b = int(s[2:])

    ans = ''
    if 1 <= f <= 12:
        ans += 'MM'
    else:
        ans += 'YY'

    if 1 <= b <= 12:
        ans += 'MM'
    else:
        ans += 'YY'

    if ans == 'MMMM':
        print('AMBIGUOUS')
        return
    elif ans == 'YYYY':
        print('NA')
        return

    print(ans)



if __name__ == '__main__':
    main()
