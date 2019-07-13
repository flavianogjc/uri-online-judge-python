from sys import stdin, stdout
from fractions import gcd

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        try:
            x, y = map(int, read_line().split())
        except ValueError:
            break

        mdc = gcd(x, y)
        x, y = x // mdc, y // mdc

        printf("%d\n" % ((x + y) << 1))
