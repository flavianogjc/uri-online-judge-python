from fractions import gcd

if __name__ == '__main__':
    while True:
        try:
            azuis, pretas, n = map(int, raw_input().split())

            d = gcd(azuis, pretas)
            azuis //= d
            pretas //= d

            if (azuis + pretas) >= n:
                print("sim")
            else:
                print("nao")
        except EOFError:
            break
