if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            adota = 0

            for i in range(0, n):
                pet = raw_input()
                race = raw_input()
                names = raw_input().split(' ')
                empy = raw_input()

                len_name = len(names)
                if pet == 'cachorro' and len_name >= 2:
                    for name in names:
                        if race[0] == name[0]:
                            adota += 1
                            break
            print adota
        except EOFError:
            break
