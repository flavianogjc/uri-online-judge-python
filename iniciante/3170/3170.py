if __name__ == '__main__':
    b = input()
    g = input()
    r = (g - 2 * b) // 2

    if r > 0:
        print('Faltam {} bolinha(s)'.format(r))
    else:
        print('Amelia tem todas bolinhas!')