if __name__ == '__main__':
    while True:
        try:
            n = input()
            for i in xrange(n // 2 + 1):
                print ' ' * (n // 2 - i) + '*' * (2 * i + 1)
            for i in xrange(2):
                print ' ' * (n // 2 - i) + '*' * (2 * i + 1)
            print
        except EOFError:
            break
