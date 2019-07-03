from math import log as ln

stirling = lambda x: x * (ln(x) - 1) + (1.837877066409345483560 + ln(x)) * 0.5  # Formula de Stirling

if __name__ == '__main__':
    N = input()
    lucas, pedro = 0, 0  # Pontos do lucas e do pedro
    lista = []

    for i in xrange(N):
        a, b = map(float, raw_input().split('^'))
        n = float(raw_input().split('!')[0])

        exp, fat = b * ln(a), stirling(n)

        if (exp > fat):
            lucas += 1
            lista.append(True)
        else:
            pedro += 1
            lista.append(False)

    if (lucas > pedro):
        print("Campeao: Lucas!")
    elif (pedro < lucas):
        print("Campeao: Pedro!")
    else:
        print("A competicao terminou empatada!")

    for i in xrange(N):
        if (lista[i]):
            print("Rodada #" + str(i + 1) + ": Lucas foi o vencedor")
        else:
            print("Rodada #" + str(i + 1) + ": Pedro foi o vencedor")