pi = 3.141590
if __name__ == '__main__':
    a, b, c = map(float, raw_input().split())

    area = a * c / 2.0
    print("TRIANGULO: %.3f" % area)

    area = pi * c * c
    print("CIRCULO: %.3f" % area)

    area = (a + b) * c / 2.0
    print("TRAPEZIO: %.3f" % area)

    area = b * b
    print("QUADRADO: %.3f" % area)

    area = a * b
    print("RETANGULO: %.3f" % area)
