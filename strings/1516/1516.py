if __name__ == '__main__':
    while True:
        n, m = map(int, raw_input().split())
        if n == m and n == 0:
            break

        img = [raw_input() for _ in xrange(n)]
        a, b = map(int, raw_input().split())

        for txt in img:
            new_txt = ''.join([char * (b // m) for char in txt])
            for _ in xrange(a // n):
                print new_txt
        print
