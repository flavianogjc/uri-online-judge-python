if __name__ == '__main__':
    n, v, i = input(), input(), float('-inf')
    for _ in xrange(n - 1):
        i = input()
        if i > v:
            break

    if i > v:
        print('N')
    else:
        print('S')
