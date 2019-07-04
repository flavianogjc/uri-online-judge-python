if __name__ == '__main__':
    n = input()

    hora = n // 3600
    n %= 3600

    minu = n // 60
    n %= 60

    seg = n

    print("%d:%d:%d" % (hora, minu, seg))
