if __name__ == '__main__':
    T = input()
    while T:
        A, B, C = map(float, raw_input().split())
        x = -B / (2. * A)

        print("%.2f" % ((A * x + B) * x + C))

        T -= 1
