# https://atcoder.jp/contests/abc007/tasks/abc007_3

# BFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque

    r, c = inp()
    sy, sx = inp()
    sy -= 1
    sx -= 1
    gy, gx = inp()
    gy -= 1
    gx -= 1
    cll = []
    for _ in range(r):
        cll.append(list(inp(False)[0]))

    dist = [[-1] * c for _ in range(r)]
    dist[sy][sx] = 0

    dq = deque()
    dq.append((sy, sx))
    while dq:
        y, x = dq.popleft()
        for dy, dx in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            vy = y + dy
            vx = x + dx
            if not ((0 <= vy < r) and (0 <= vx < c)):
                continue

            if cll[vy][vx] == '#':
                continue

            if not dist[vy][vx] == -1:
                continue

            dist[vy][vx] = dist[y][x] + 1
            dq.append((vy, vx))

    print(dist[gy][gx])


if __name__ == '__main__':
    main()
