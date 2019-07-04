if __name__ == '__main__':
    a, b, c = map(int, raw_input().split())

    m = (a + b + abs(a - b)) >> 1
    m = (c + m + abs(c - m)) >> 1

    print("%d eh o maior" % m);
