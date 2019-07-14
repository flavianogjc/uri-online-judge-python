dicionario = {'zero': 0, 'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9,
       'dez': 10, 'onze': 11, 'doze': 12, 'treze': 13, 'quatorze': 14, 'quinze': 15, 'dezesseis': 16, 'dezessete': 17,
       'dezoito': 18, 'dezenove': 19,
       'vinte': 20, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50, 'sessenta': 60, 'setenta': 70, 'oitenta': 80,
       'noventa': 90,
       'cem': 100, 'cento': 100, 'duzentos': 200, 'trezentos': 300, 'quatrocentos': 400, 'quinhentos': 500,
       'seiscentos': 600, 'setecentos': 700,
       'oitocentos': 800, 'novecentos': 900,
       'mil': 1000, 'milhao': 10 ** 6, 'milhoes': 10 ** 6, 'bilhao': 10 ** 9, 'bilhoes': 10 ** 9, 'trilhao': 10 ** 12,
       'trilhoes': 10 ** 12
              }

if __name__ == '__main__':
    while True:
        try:
            digts = []
            for name in raw_input().split():
                if name in dicionario:
                    digts.append(dicionario[name])

            length = len(digts)
            num, aux = (digts[0], 0) if length == 1 else (0, digts[0])
            for idx in xrange(1, length):
                if digts[idx] < digts[idx - 1]:
                    aux += digts[idx]
                else:
                    num += aux * digts[idx]
                    aux = 0
            print(num + aux)
        except EOFError:
            break
