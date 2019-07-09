from sys import stdin, stdout
from math import log, floor

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797]


def factor(n):
    p, r = [], []
    for i in primes:
        if n % i == 0:
            p.append(i)
            v = 0
            while n % i == 0:
                v += 1
                n //= i
            r.append(v)

        if n == 1:
            break

    return p, r


def cont_zeros(n, b):
    p, r = factor(b)

    k, lenP = float('inf'), len(p)
    for i in xrange(lenP):
        kp, power = 0, p[i]
        while n // power:
            kp += n / power
            power *= p[i]

        if (kp // r[i]) < k:
            k = kp // r[i]

    return k


read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        try:
            n, base = map(int, read_line().split())

            l = 0
            for i in xrange(1, n + 1):
                l += log(i) / log(base)
            nDigt = floor(l) + 1

            printf("%d %d\n"%(cont_zeros(n, base), nDigt))
        except ValueError:
            break