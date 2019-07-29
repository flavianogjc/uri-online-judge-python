if __name__ == '__main__':
    n = input()

    for i in xrange(n):
        x = [0] * 7

        x[0] = input()
        x[2], x[3], x[4], x[5] = map(int, raw_input().split())
        x[1] = input()

        if x[0] + x[1] == 7 and x[2] + x[4] == 7 and x[3] + x[5] == 7:
            if 1 in x and 2 in x and 3 in x and 4 in x and 5 in x and 6 in x:
                print("SIM")
            else:
                print("NAO")
        else:
            print("NAO")
