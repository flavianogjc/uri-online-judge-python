from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    n = int(read_line())
    resp = {
        'A': 0,
        'E': 0,
        'H': 0,
        'M': 0,
        'X': 0
    }
    for _ in xrange(n):
        a = read_line().split()
        resp[a[-1]] += 1

    printf('{} Hobbit(s)\n{} Humano(s)\n{} Elfo(s)\n{} Anao(s)\n{} Mago(s)\n'.format(*[resp[r] for r in 'XHEAM']))
