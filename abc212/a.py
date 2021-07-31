def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    a, b = inp()
    if 0 < a and b == 0:
        print('Gold')
    elif a == 0 and 0 < b:
        print('Silver')
    elif 0 < a and 0 < b:
        print('Alloy')


if __name__ == '__main__':
    main()
