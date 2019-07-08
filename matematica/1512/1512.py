from fractions import gcd

lcd = lambda x, y: (x * y) // gcd(x, y)


def func(n, a, b):
    return (n // a) + (n // b) - (n // lcd(a, b))


if __name__ == '__main__':
    while True:
        N, A, B = map(int, raw_input().split())

        if N == 0 and A == 0 and B == 0:
            break
        else:
            print(func(N, A, B))
