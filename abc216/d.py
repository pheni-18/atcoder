def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque
    n, m = inp()
    cl = {}
    for i in range(n):
        cl[i + 1] = []

    dq = deque()
    all = []
    kl = []
    for i in range(m):
        k = inp()[0]
        kl.append(k)
        al = inp()
        all.append(al)

        cl[al[0]].append(i)
        if len(cl[al[0]]) == 2:
            dq.append(al[0])

    curl = [0] * m
    cnt = 0
    while dq:
        a = dq.popleft()
        for i in cl[a]:
            curl[i] += 1
            cur = curl[i]
            al = all[i]
            if cur >= kl[i]:
                continue

            cl[al[cur]].append(i)
            if len(cl[al[cur]]) == 2:
                dq.append(al[cur])

        cnt += 1

    if cnt == n:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
