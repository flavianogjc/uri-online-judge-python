from sys import stdin, stdout
from math import sin, cos, sqrt


def ponto_de_impacto(h, v, a):
    a *= pi / 180  # Pra radiano

    return v * cos(a) * (v * sin(a) + sqrt(v * v * sin(a) * sin(a) + 2.0 * h * g)) / g


read_line = stdin.readline
printf = stdout.write
pi = 3.14159  # rad
g = 9.80665  # m/s**2
if __name__ == '__main__':
    while True:
        try:
            h = float(raw_input())
            p1, p2 = map(int, raw_input().split())

            n = input()
            for i in xrange(n):
                ang, speed = map(float, raw_input().split())

                p = ponto_de_impacto(h, speed, ang)
                if p1 <= p and p <= p2:
                    txt = " -> DUCK"
                else:
                    txt = " -> NUCK"

                printf("%.5f%s\n" % (p, txt))
        except EOFError:
            break
