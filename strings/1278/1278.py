if __name__ == '__main__':
    start = False
    while True:
        n = input()
        if n == 0:
            break
        if start:
            print

        words = [' '.join(map(str, raw_input().split())) for _ in xrange(n)]
        max_length = len(max(words, key=len))
        for word in words:
            print ' ' * (max_length - len(word)) + word

        start = True
