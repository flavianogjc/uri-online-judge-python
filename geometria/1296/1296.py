from math import sqrt

if __name__ == '__main__':
    while True:
        try:
            ma, mb, mc = map(float, raw_input().split())

            M = (ma + mb + mc) / 2.00
            p = M * (M - ma) * (M - mb) * (M - mc)

            if p > 0:
                p = (4.0 / 3.0) * sqrt(p)
                print("%.3f" % p)
            else:
                print("%.3f" % -1.000)
        except EOFError:
            break
