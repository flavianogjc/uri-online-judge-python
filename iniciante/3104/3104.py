from sys import stdin, stdout


def rest(num_a, num_b):
    dg = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    r = dg.get(num_a[-1]) % num_b
    p = 1
    for i in xrange(len(num_a) - 2, -1, -1):
        p = (10 * p) % num_b
        r = (dg.get(num_a[i]) * p + r) % num_b
    return r


read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    a = read_line()[:-1]
    b = int(read_line())
    printf('%d\n' % rest(a, b))
