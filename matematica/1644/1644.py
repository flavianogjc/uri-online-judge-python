from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while (True):
        N, M = map(int, read_line().split())
        if (N == 0 and M == 0):
            break

        q, p = map(lambda x: int(x) - 1, read_line().split()), [None] * N
        for i in xrange(N):
            p[q[i]] = i

        textCifrado, textPuro = read_line(), list(textCifrado)

        for i in xrange(N):
            if (p[i] == i):
                continue
            temp = []
            while (p[i] != i):
                temp.append(p[i])
                aux = p[i]
                p[i] = p[p[i]]
                p[aux] = aux
            temp.append(p[i])

            sizeTemp = len(temp)
            k = M % sizeTemp
            for j in xrange(sizeTemp):
                textPuro[temp[j]] = textCifrado[temp[(j + k) % sizeTemp]]
        printf(''.join(textPuro))