from sys import stdin, stdout

scanf = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        lista = map(lambda x: int(x) - 1, scanf().split())
        N = lista[0] + 1
        if not N:
            break

        del lista[0]

        p, i = 0, 0
        while i < N:
            if lista[i] != i:
                p += (abs(lista[i] - i) << 1) - 1
                p &= 1

                aux = lista[lista[i]]
                lista[lista[i]] = lista[i]
                lista[i] = aux
                i -= 1
            i += 1

        if p & 1:
            printf("Marcelo\n")
        else:
            printf("Carlos\n")
