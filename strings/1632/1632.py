if __name__ == '__main__':
    special_chars = ['a', '4', 'e', '3', 'i', '1', 'o', '0', 's', '5']
    for _ in xrange(input()):
        s = raw_input().lower()
        n = sum([char in special_chars for char in s])
        print 2 ** (len(s) - n) * 3 ** n
