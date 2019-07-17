if __name__ == '__main__':
    while True:
        try:
            input()
        except EOFError:
            break

        num = []
        while True:
            try:
                num.append(map(str, raw_input().split())[1])
            except IndexError:
                break
        num.sort()

        for i in num:
            print("".join(["Package ", i]))

        print("")
