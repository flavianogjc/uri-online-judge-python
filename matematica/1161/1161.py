from math import factorial as fat

if __name__ == '__main__':
    while (True):
        try:
            n, m = map(int, raw_input().split())
            print(fat(n) + fat(m))
        except:
            break
