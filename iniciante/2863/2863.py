if __name__ == '__main__':
    while True:
        try:
            n = input()
        except EOFError:
            break

        m = 13
        for i in xrange(n):
            f = float(raw_input())
            if f < m:
                m = f

        print(m)
