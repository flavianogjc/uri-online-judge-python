# Gambler's ruin

if __name__ == '__main__':
    while (True):
        EV1, EV2, AT, D = map(int, raw_input().split())
        if (EV1 == 0 and EV2 == 0 and AT == 0 and D == 0):
            break

        n1 = EV1 / D + (1 if (EV1 % D) else 0)
        n2 = EV2 / D + (1 if (EV2 % D) else 0)

        if (AT == 3):
            print("%.1lf" % (n1 * 100.0 / (n1 + n2)))
        else:
            p = AT / 6.0
            q = 1 - p
            r = q / p

            p1 = r ** n1
            p2 = p1 * r ** n2

            print("%.1lf" % ((1.0 - p1) / (1.0 - p2) * 100.0))
