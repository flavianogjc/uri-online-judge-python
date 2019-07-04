if __name__ == '__main__':
    a, b, c = map(float, raw_input().split())
    x, y, z = map(float, raw_input().split())

    print("VALOR A PAGAR: R$ %.2f" % (b * c + y * z))
