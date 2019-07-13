def check(x, y):
    if x <= y:
        if x < y:
            return -1
        else:
            return 0
    else:
        return 1


if __name__ == '__main__':
    N = input()

    tang_1, tang_2 = -1., float('inf')
    for i in xrange(N):
        d, a, b = map(float, raw_input().split())

        if a / d > tang_1:
            tang_1 = a / d
        if b / d < tang_2:
            tang_2 = b / d

    D, A, B = map(float, raw_input().split())
    Y1, Y2 = tang_1 * D, tang_2 * D

    acerta = (check(Y2, A) != -1) and (check(Y1, B) != 1) and (check(Y1, Y2) != 1)
    if acerta:
        print('Y')
    else:
        print('N')
