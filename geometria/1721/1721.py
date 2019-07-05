from math import sqrt, acos, pi, cos, sin, radians

R = 6378.0  # Raio da terra [Km]
if __name__ == '__main__':
    cities = dict()
    while True:
        txt = raw_input()
        if txt != "#":
            txt = txt.split()
            la, lo = map(float, txt[1:]) # Latitude e Longitude

            # Coordenada esferica para cartesiana
            x = cos(radians(la)) * sin(radians(lo))
            y = cos(radians(la)) * cos(radians(lo))
            z = sin(radians(la))

            cities[txt[0]] = [x, y, z]
        else:
            break

    while True:
        txt = raw_input()
        if txt != "#":
            a, b, c = txt.split()
            if (a not in cities) or (b not in cities) or (c not in cities):
                print("%s is ? km off %s/%s equidistance." % (c, a, b))
                continue

            # Vetor normal ao plano equidistante
            x, y, z = cities[a][0] - cities[b][0], cities[a][1] - cities[b][1], cities[a][2] - cities[b][2]
            cx, cy, cz = cities[c][0], cities[c][1], cities[c][2]

            # Angulo entre vetor cidade(c) e vetor normal
            try:
                th = acos((cx * x + cy * y + cz * z) / sqrt(x * x + y * y + z * z))
            except (ZeroDivisionError, ValueError):
                th = acos(cx * x + cy * y + cz * z)

            # Angulo entre vetor cidade(c) e plano equidistante
            th = abs(.5 * pi - th)

            d = th * R
            print("%s is %d km off %s/%s equidistance." % (c, round(d), a, b))
        else:
            break
