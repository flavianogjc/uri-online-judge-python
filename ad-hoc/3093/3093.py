if __name__ == '__main__':
    for _ in xrange(input()):
        s = set(raw_input())
        if all([l in s for l in 'QJKA']):
            print 'Aaah muleke'
        else:
            print 'Ooo raca viu'
