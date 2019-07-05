if __name__ == '__main__':
    n = input()

    ano = n // 365
    n %= 365

    mes = n // 30
    n %= 30

    dia = n

    print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (ano, mes, dia))
