if __name__ == '__main__':
    while True:
        try:
            a = input()

            if a % 6:
                print('N')
            else:
                print('Y')
        except EOFError:
            break
