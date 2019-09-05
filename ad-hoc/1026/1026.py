if __name__ == '__main__':
    while True:
        try:
            a, b = map(int, raw_input().split())
            print(a ^ b)
        except EOFError:
            break
