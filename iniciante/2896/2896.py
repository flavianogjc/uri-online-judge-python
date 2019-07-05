from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    for i in xrange(input()):
        N, K = map(int, read_line().split())
        printf("%d\n" % ((N // K) + (N % K)))
