from fractions import gcd

if __name__ == '__main__':
    while (True):
        try:
            n = input()
            for i in xrange(n):
                a, b = map(int, raw_input().split())

                print(gcd(a, b))
        except:
            break
