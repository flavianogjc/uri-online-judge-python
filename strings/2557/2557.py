if __name__ == '__main__':
    while True:
        try:
            line = raw_input()
            a = line.split('+')
            b = a[1].split('=')

            if a[0] == 'R':
                resp = int(b[1]) - int(b[0])
            elif b[0] == 'L':
                resp = int(b[1]) - int(a[0])
            else:
                resp = int(a[0]) + int(b[0])

            print(resp)
        except EOFError:
            break
