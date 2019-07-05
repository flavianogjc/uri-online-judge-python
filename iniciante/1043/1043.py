if __name__ == '__main__':
    a, b, c = map(float, raw_input().split())

    area = 0.50 * (a + b) * c
    if (a >= (b + c)):
        print("Area = %.1lf" % area)
    elif (b >= (a + c)):
        print("Area = %.1lf" % area)
    elif (c >= (a + b)):
        print("Area = %.1lf" % area)
    else:
        print("Perimetro = %.1lf" % (a + b + c))
