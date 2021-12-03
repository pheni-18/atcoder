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
    if N < 10:
        print(f'AGC00{N}')
    elif N < 42:
        print(f'AGC0{N}')
    else:
        print(f'AGC0{N + 1}')


if __name__ == '__main__':
    main()
