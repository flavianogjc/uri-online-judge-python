if __name__ == '__main__':
    a, g, ra, rg = map(float, raw_input().split())
    if a / ra < g / rg:
        print 'A'
    else:
        print 'G'
