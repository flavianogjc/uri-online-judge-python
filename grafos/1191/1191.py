from sys import stdout


def recursion(i, j):
    global curr, prefixo, infixo

    if i <= j:
        curr += 1

        pos = infixo.index(prefixo[curr])

        recursion(i, pos - 1)
        recursion(pos + 1, j)

        printf(infixo[pos])
    else:
        return None

    return None


def solver():
    global curr, prefixo, infixo

    curr = -1
    recursion(0, len(infixo) - 1)
    printf('\n')

    return None


printf = stdout.write
if __name__ == '__main__':
    curr = -1

    while True:
        try:
            prefixo, infixo = map(str, raw_input().split())
        except:
            break

        solver()
