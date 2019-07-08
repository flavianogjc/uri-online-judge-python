from math import tan
from sys import stdout

printf = stdout.write
if __name__ == '__main__':
    while True:
        try:
            a, d, r = map(float, raw_input().split())

            if r < 90.0:
                x = tan(1.570797 - 0.0174533 * r)
                printf("%.4f\n" % (a - d * x))
            elif r == 90.00:
                printf("%.4f\n" % a)
            else:
                x = tan(0.0174533 * r - 1.570797)
                printf("%.4f\n" % (a + d * x))
        except EOFError:
            break
