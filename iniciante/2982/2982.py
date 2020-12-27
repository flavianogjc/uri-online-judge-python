if __name__ == '__main__':
    n = input()
    total = 0
    for _ in xrange(n):
        t, c = raw_input().split()
        total += int(c) if t == 'V' else -int(c)

    if total >= 0:
        print('A greve vai parar.')
    else:
        print('NAO VAI TER CORTE, VAI TER LUTA!')
