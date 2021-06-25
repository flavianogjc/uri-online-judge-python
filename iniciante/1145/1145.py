x, y = map(int, raw_input().split())

if __name__ == '__main__':
    i = 1
    while i <= y:
        print(' '.join(map(str, xrange(i, i + x))))
        i += x
