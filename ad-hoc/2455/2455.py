if __name__ == '__main__':
    a, b, c, d = map(int, raw_input().split())

    if a * b == c * d:
        print 0
    elif a * b < c * d:
        print 1
    else:
        print -1
