if __name__ == '__main__':
    M = input()

    for i in xrange(M):
        a, b = map(int, raw_input().split())
        z = complex(a, b)
        complicado, n = False, 0

        zn = 1  # zn = z**n
        while (True):
            zn *= z
            n += 1
            if (abs(zn) > 0x40000000):
                complicado = True
                break
            elif (zn.imag == 0.0):
                break
        if (complicado):
            print("TOO COMPLICATED")
        else:
            print(n)