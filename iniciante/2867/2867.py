from math import log10 as log

for i in xrange(input()):
    n, m = map(float, raw_input().split())
    print(int(m * log(n) + 1.))
