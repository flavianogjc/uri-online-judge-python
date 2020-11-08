if __name__ == '__main__':
    for _ in xrange(input()):
        h, k = map(lambda a: a.count('a'), raw_input().split('k'))
        print 'k' + 'a' * (h * k)
