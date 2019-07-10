def validator(num):
    v1, v2, i = 0, 0, 1
    for d in map(int, num):
        v1 += d * i
        v2 += d * (10 - i)
        i += 1

    v1 = (v1 % 11) % 10
    v2 = (v2 % 11) % 10

    return str(v1) + str(v2)


if __name__ == '__main__':
    while True:
        try:
            num, val = raw_input().split("-")
            num = num.replace(".", "")
        except EOFError:
            break

        if validator(num) == val:
            print("CPF valido")
        else:
            print("CPF invalido")
