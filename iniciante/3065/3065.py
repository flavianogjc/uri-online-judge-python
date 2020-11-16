if __name__ == '__main__':
    test = 1
    while input():
        exp = raw_input()
        print 'Teste {}'.format(test)
        print eval(exp)
        print
        test += 1
