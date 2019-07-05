if __name__ == '__main__':
    a, b = map(int, raw_input().split())

    if (a % b == 0 or b % a == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
