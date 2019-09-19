# https://oeis.org/A006008

if __name__ == '__main__':
    while True:
        n = input()
        if n == 0:
            break
        n2 = n * n
        n4 = n2 * n2

        print ((11 * n2 + n4) / 12) % 1000007
