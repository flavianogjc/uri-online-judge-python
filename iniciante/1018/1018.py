if __name__ == '__main__':
    money = input()
    
    print(money)

    n100 = money // 100  # Notas de R$ 100
    money %= 100

    n50 = money // 50  # Notas de R$ 50
    money %= 50

    n20 = money // 20  # Notas de R$ 20
    money %= 20

    n10 = money // 10  # Notas de R$ 10
    money %= 10

    n5 = money // 5  # Notas de R$ 5
    money %= 5

    n2 = money // 2  # Notas de R$ 2
    money %= 2

    n1 = money  # Notas de R$ 1

    print("%d nota(s) de R$ 100,00" % n100)
    print("%d nota(s) de R$ 50,00" % n50)
    print("%d nota(s) de R$ 20,00" % n20)
    print("%d nota(s) de R$ 10,00" % n10)
    print("%d nota(s) de R$ 5,00" % n5)
    print("%d nota(s) de R$ 2,00" % n2)
    print("%d nota(s) de R$ 1,00" % n1)
