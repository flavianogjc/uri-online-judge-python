if __name__ == '__main__':
    while True:
        try:
            v, t = map(int, raw_input().split())
            print(2 * v * t)
        except EOFError:
            break
