from sys import stdin, stdout
from math import sqrt

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        try:
            r1, x1, y1, r2, x2, y2 = map(int, read_line().split())

            d = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
            if r1 >= (d + r2):
                printf('RICO\n')
            else:
                printf('MORTO\n')
        except ValueError:
            break