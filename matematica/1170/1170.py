from math import log, ceil

log2 = lambda x: log(x, 2)
if __name__ == '__main__':
    n = input()
    for i in xrange(n):
        c = float(raw_input())

        dias = ceil(log2(c))
        print("%d dias" % dias)
