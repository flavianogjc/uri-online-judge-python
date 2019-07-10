def validator(num):
    v1, v2, i = 0, 0, 1
    cpf = ""
    for d in map(int, num):
        v1 += d * i
        v2 += d * (10 - i)
        cpf += str(d) + ("." if (i % 3 == 0 and i != 9) else "")
        i += 1

    v1 = (v1 % 11) % 10
    v2 = (v2 % 11) % 10

    return cpf + "-" + str(v1) + str(v2)


if __name__ == '__main__':
    while True:
        try:
            n = raw_input()
        except EOFError:
            break

        print(validator(n))