from math import ceil

if __name__ == '__main__':
    a, b = map(float, raw_input().split())
    r = ceil(b / (b - a))

    print(int(r))
