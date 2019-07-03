from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while (True):
        S, N, M = map(int, read_line().split())

        if (S == 0 and N == 0 and M == 0):
            break

        C1, C2, C3 = map(int, read_line().split())

        N += 1
        M += 1

        s = (S * C1 * abs(C3 - C2)) / (N * M)

        printf("%d\n" % (s))
