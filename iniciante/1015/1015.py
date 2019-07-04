from math import sqrt

if __name__ == '__main__':
    x1, y1 = map(float, raw_input().split())
    x2, y2 = map(float, raw_input().split())

    d2 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
    d = sqrt(d2)

    print("%.4lf" % d)
