from math import pi

if __name__ == '__main__':
    while (True):
        w, h = map(float, raw_input().split())

        if (w == 0 and h == 0):
            break
        elif (w * (pi + 1) <= h):
            volume1 = (w * w / (4.0 * pi)) * (h - (w / pi))
            volume2 = pi * w * w * w / 4.0
            if (volume1 > volume2):
                print("%.3lf" % volume1)
            else:
                print("%.3lf" % volume2)
        else:
            volume1 = (w * w / (4.0 * pi)) * (h - (w / pi))
            volume2 = pi * h * h * w / (4.0 * (pi + 1.0) * (pi + 1.0))
            if (volume1 > volume2):
                print("%.3lf" % volume1)
            else:
                print("%.3lf" % volume2)
