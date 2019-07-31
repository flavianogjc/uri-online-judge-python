if __name__ == '__main__':
    C = input()

    for a in xrange(C):
        N = input()

        X, Y = map(int, raw_input().split())

        d = float("inf")
        i = 1
        for b in xrange(N):
            x, y = map(int, raw_input().split())

            D = (x - X) * (x - X) + (y - Y) * (y - Y)
            if D < d:
                d = D
                index = i
            i += 1

        print(index)
