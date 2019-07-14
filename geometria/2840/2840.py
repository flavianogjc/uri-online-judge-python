from math import floor

if __name__ == '__main__':
    r, l = map(float, raw_input().split())

    v_esfera = (4.188666) * r * r * r # Volume da esfera
    v_botijao = l   # Volume do botijão..

    print(int(floor(v_botijao / v_esfera)))
