# https://atcoder.jp/contests/abc088/tasks/abc088_d

# BFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque
    h, w = inp()
    sll = []
    white_cnt = 0
    for _ in range(h):
        sl = list(inp(False)[0])
        white_cnt += sl.count('.')
        sll.append(sl)

    dist = [[-1] * w for _ in range(h)]
    dist[0][0] = 0
    dq = deque()
    dq.append((0, 0))
    while dq:
        y, x = dq.popleft()

        for dy, dx in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            vy = y + dy
            vx = x + dx
            if not ((0 <= vy < h) and (0 <= vx < w)):
                continue

            if sll[vy][vx] == '#':
                continue

            if not dist[vy][vx] == -1:
                continue

            dist[vy][vx] = dist[y][x] + 1
            dq.append((vy, vx))

    goal_dist = dist[h - 1][w - 1]
    if goal_dist == -1:
        print(-1)
        return

    print(white_cnt - goal_dist - 1)


if __name__ == '__main__':
    main()
