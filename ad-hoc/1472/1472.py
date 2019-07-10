from bisect import bisect_left
from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write


def search(item):
    return (item <= soma[-1]) and (soma[bisect_left(soma, item)] == item)


if __name__ == '__main__':
    while True:
        try:
            n = int(read_line())
            arc = map(int, read_line().split())

            soma, total = [], 0
            for i in arc:
                total += i
                soma.append(total)

            if total % 3 != 0:
                print 0
            else:
                arc = total / 3
                arc2 = arc << 1
                triangulos, i = 0, 0
                for i in xrange(n):
                    if soma[i] > arc:
                        break
                    if search(soma[i] + arc) and search(soma[i] + arc2):
                        triangulos += 1
                printf("%d\n" % triangulos)
        except EOFError:
            break
