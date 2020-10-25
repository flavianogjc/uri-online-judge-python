from sys import stdin, stdout

base = 1 << 32
scanf = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    T = input()
    while T:
        N, K = map(int, scanf().split())
        num_list = map(int, scanf().split())

        table = [0] * 33
        for i in xrange(N):
            for j in xrange(32):
                if (num_list[i] >> j) % 2:
                    table[j] = (table[j] | (1 << i) % base)

        bigger, p = 0, (1 << N) % base - 1
        for i in xrange(32, -1, -1):
            if (bin(p & table[i]).count('1')) >= K:
                bigger = (bigger | (1 << i) % base)
                p = (p & table[i]) % base

        printf('%d\n' % bigger)

        T -= 1
