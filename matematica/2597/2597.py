from math import sqrt

if __name__=='__main__':
    n = input()
    for i in xrange(n):
        m = input()
        print(m-int(sqrt(m)))