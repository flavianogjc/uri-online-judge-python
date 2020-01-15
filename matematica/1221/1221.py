def find_primes():
    primes[0] = 2

    i = 1
    for j in xrange(3, 46341):
        for k in xrange(0, i):
            if not (j % primes[k]):
                break
        k += 1
        if k==i:
            primes[i] = j
            i += 1


primes = [0] * 4792 # Lista dos primos
if __name__ == '__main__':
    find_primes()

    n = input()
    for i in xrange(n):
        m = input()
        for j in xrange(len(primes)):
            if not (m % primes[j]) and m != primes[j]:
                print('Not Prime')
                break

        if j + 1 == len(primes):
            print('Prime')

