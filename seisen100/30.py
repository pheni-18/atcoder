# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

# BFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque
    h, w, n = inp()
    all = []
    sy, sx = -1, -1
    for i in range(h):
        al = list(inp(False)[0])
        for j in range(w):
            if al[j] == 'S':
                sy, sx = i, j

        all.append(al)

    def reset_dist(y, x):
        nonlocal dist
        dist = [[-1] * w for _ in range(h)]
        dist[y][x] = 0

    hp = 1
    ans = 0
    dist = []
    reset_dist(sy, sx)
    dq = deque()
    dq.append((sy, sx))
    while dq:
        y, x = dq.popleft()
        if all[y][x] == str(hp):
            ans += dist[y][x]
            if int(all[y][x]) == n:
                break

            dq.clear()
            dq.append((y, x))
            hp += 1
            reset_dist(y, x)

        for dy, dx in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            vy = y + dy
            vx = x + dx
            if not ((0 <= vy < h) and (0 <= vx < w)):
                continue

            if all[vy][vx] == 'X':
                continue

            if not dist[vy][vx] == -1:
                continue

            dist[vy][vx] = dist[y][x] + 1
            dq.append((vy, vx))

    print(ans)


if __name__ == '__main__':
    main()
