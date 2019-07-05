if __name__ == '__main__':
    a, b, c = map(int, raw_input().split())
    x, y, z = a, b, c

    if (a > b):
        a, b = b, a

    if (a > c):
        a, c = c, a

    if (b > c):
        b, c = c, b

    print("%d\n%d\n%d\n" % (a, b, c))
    print("%d\n%d\n%d" % (x, y, z))
