if __name__ == '__main__':
    n = input()
    antes, flag = 0, False
    for p in map(int, raw_input().split()):
        if p - antes > 8:
            flag = True
        antes = p

    print('N' if (flag) else 'S')
