def calc():
    for j in xrange(8, -1, -1):
        if a >= arr[j]:
            c = a / arr[j]
            d = a % arr[j]
            e = c % 10
            c /= 10

            for i in xrange(0, e):
                resp[i] += arr[j] * (c + (1 if i else 0))

            resp[e] += arr[j] * (c - (0 if e else 1)) + d + 1

            for i in xrange(e + 1, 10):
                resp[i] += arr[j] * c

    return None


def calc2():
    for j in xrange(8, -1, -1):
        if b >= arr[j]:
            c = b / arr[j]
            d = b % arr[j]
            e = c % 10
            c /= 10

            for i in xrange(0, e):
                resp[i] -= arr[j] * (c + (1 if i else 0))

            resp[e] -= arr[j] * (c - (0 if e else 1)) + d + 1

            for i in xrange(e + 1, 10):
                resp[i] -= arr[j] * c

    return None


arr = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
if __name__ == '__main__':
    while True:
        a, b = map(int, raw_input().split())

        if a == 0 and b == 0:
            break

        resp = [0] * 10
        a -= 1

        calc()
        calc2()

        out = str(abs(resp[0]))
        for i in xrange(1, 10):
            out += ' ' + str(abs(resp[i]))
        print(out)