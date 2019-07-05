from math import sqrt

if __name__ == '__main__':
    while True:
        try:
            w, l = map(float, raw_input().split())

            if w > l:
                w, l = l, w

            x1 = (w + l + sqrt(w * w - w * l + l * l)) / 6.0
            x2 = (w + l - sqrt(w * w - w * l + l * l)) / 6.0

            if w != l:
                print("%.3f %.3f %.3f" % (x2, 0.0, 0.5 * w))
            else:
                print("%.3f %.3f %.3f" % (x2, 0.0, x1))
        except EOFError:
            break
