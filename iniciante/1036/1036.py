from math import sqrt

if __name__ == '__main__':
    a, b, c = map(float, raw_input().split())

    delta = b * b - 4.0 * a * c
    if (a == 0 or delta < 0):
        print("Impossivel calcular")
    else:
        d = sqrt(delta)
        r1 = (-b + d) / (2.0 * a)
        r2 = -(b + d) / (2.0 * a)

        print("R1 = %.5f" % r1)
        print("R2 = %.5f" % r2)
