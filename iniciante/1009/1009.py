if __name__ == '__main__':
    raw_input()

    salario = float(raw_input())
    vendas = float(raw_input())

    total = salario + 0.15 * vendas
    print("TOTAL = R$ %.2f" % total)
