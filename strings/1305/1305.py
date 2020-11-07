import math

if __name__ == '__main__':
    while True:
        try:
            num = float(raw_input())
            cutoff = float(raw_input())
            frac, whole = math.modf(num)

            if cutoff < frac:
                print int(whole) + 1
            else:
                print int(whole)
        except EOFError:
            break
