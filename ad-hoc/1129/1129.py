gabarito = ('A', 'B', 'C', 'D', 'E')
if __name__ == '__main__':
    while True:
        n = input()
        if n == 0:
            break

        for i in xrange(n):
            resp = map(lambda x: int(x) <= 127, raw_input().split())

            if sum(resp) == 1:
                print(gabarito[resp.index(True)])
            else:
                print("*")
