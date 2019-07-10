if __name__ == '__main__':
    while True:
        try:
            N = input()
        except EOFError:
            break

        txt = (chr(int(raw_input(), 2)) for i in xrange(N))
        print("".join(txt))
