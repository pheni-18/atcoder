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
    S = inp_one(False)
    t = 'oxx' * 10 ** 5

    ans = 'No'
    len_s = len(S)
    for i in range(len(t)):
        if S == t[i:i+len_s]:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()
