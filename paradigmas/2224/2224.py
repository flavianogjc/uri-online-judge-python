from math import sqrt


def dist(i, j):
    global x, y

    h = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])

    return sqrt(h)


def pair_up(mask):
    global n, ready

    if mask == (1 << n) - 1:
        return 0
    if ready[mask] != 0:
        return ready[mask]

    answer = float('inf')

    last_p1 = 0
    for p1 in xrange(n):
        if not (1 & (mask >> p1)):
            last_p1 = p1
            break

    for p2 in xrange(last_p1 + 1, n):
        if not (1 & (mask >> p2)):
            answer = min(answer, dist(last_p1, p2) + pair_up(mask | (1 << last_p1) | (1 << p2)))

    ready[mask] = answer

    return answer


if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        x, y = [], []
        for _ in xrange(n):
            a, b = map(int, raw_input().split())
            x.append(a)
            y.append(b)
        ready = [0] * 65536

        ans = pair_up(0)

        print("%.2f" % ans)
